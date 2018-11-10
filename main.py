import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import config

vk_session = vk_api.VkApi(config.login, config.password, config.token)
vk_session.auth(token_only=True)
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)



for event in longpoll.listen():
    if(event.type == VkEventType.MESSAGE_NEW):
        print(event)
        print(event.text)
        # print(event.payload)
        print(event.attachments)