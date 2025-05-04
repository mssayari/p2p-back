from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
from models.message import Message
from extensions import db

messages_bp = Blueprint('messages', __name__)


@messages_bp.route('/messages', methods=['POST'])
@jwt_required()
def send_message():
    current_user_email = get_jwt_identity()
    sender = User.query.filter_by(email=current_user_email).first()

    if not sender:
        return jsonify({"success": False, "message": "Sender not found"}), 404

    data = request.json
    receiver = User.query.filter_by(id=data.get('receiver_id')).first()

    if not receiver:
        return jsonify({"success": False, "message": "Receiver not found"}), 404

    if not data.get('content'):
        return jsonify({"success": False, "message": "Message content is required"}), 400

    message = Message(sender_id=sender.id, receiver_id=receiver.id, content=data['content'])
    db.session.add(message)
    db.session.commit()

    return jsonify({"success": True, "message": "Message sent successfully"}), 201


@messages_bp.route('/messages/<int:user_id>', methods=['GET'])
@jwt_required()
def get_messages(user_id):
    current_user_email = get_jwt_identity()
    current_user = User.query.filter_by(email=current_user_email).first()

    if not current_user:
        return jsonify({"success": False, "message": "User not found"}), 404

    messages = Message.query.filter(
        (Message.sender_id == current_user.id) & (Message.receiver_id == user_id) |
        (Message.sender_id == user_id) & (Message.receiver_id == current_user.id)
    ).order_by(Message.timestamp).all()

    messages_list = [message.to_dict() for message in messages]

    return jsonify({"success": True, "messages": messages_list}), 200
