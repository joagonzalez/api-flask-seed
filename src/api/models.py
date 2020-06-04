from flask_restx import fields

message_model_definition = {
                            'message': fields.String('Body of the message to send'),
                            'from': fields.String('User that sends the message')
                        }
