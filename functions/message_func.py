from connect_mongodb import messages
import streamlit as st

def get_messages(sender_id, receiver_id):
    conversation = messages.find({
    "$or": [
        {
            "sender_id": sender_id,
            "receiver_id": receiver_id
        },
        {
            "sender_id": receiver_id,
            "receiver_id": sender_id
        }
    ]
    }).sort("timestamp", 1)
    return list(conversation)


def send_message(sender_id, receiver_id, message, image, timestamp):
    new_message = {
        "sender_id": sender_id,
        "receiver_id": receiver_id,
        "message": message,
        "image": image.getvalue() if image else None, 
        "timestamp": timestamp
    }

    messages.insert_one(new_message)