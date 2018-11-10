import vk_api, json

def auth(vk, id, botname, email = None):
    if email == None:
        pass
    else:
        pass

def sub(vk, id, botname, email = None):
    pass

def un_sub(vk, id, botname):
    pass

def post(vk, id, botname):
    pass

def check_permission(vk, id):
    pass

def my_info(vk, id):
    pass

def sub_info(vk, id):
    pass

def send(vk, id, botname, text = None, attachment = None):
    if not attachment:
        vk.messages.send(peer_id = id, message = botname + text)
    elif text:
        vk.messages.send(peer_id = id, message=botname + text, attachment=attachment)
    else:
        vk.messages.send(peer_id = id, message=botname, attachment=attachment)


def greeting(vk, id, botname):
    message = "Здравствуй, отсоси"
    send(vk, id, botname, text = message)

def use_promo():
    pass