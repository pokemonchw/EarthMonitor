from mastodon import Mastodon
from EarthPlugins import MessagePush,CacheHandle
import socks,socket
from bot_constant import MASTODON_CLIENT_ID,MASTODON_CLIENT_SECRET,MASTODON_ACCESS_TOKEN,MASTODON_API_BASE_URL,PROXY_IP,PROXY_PORT

def pushMessage(message):
    client_id = MASTODON_CLIENT_ID
    client_secret = MASTODON_CLIENT_SECRET
    access_token = MASTODON_ACCESS_TOKEN
    api = Mastodon(client_id, client_secret, access_token,
            api_base_url=MASTODON_API_BASE_URL)
    socksDefault = socks.get_default_proxy()
    socketDefault = socket.socket
    socks.set_default_proxy(socks.SOCKS5,PROXY_IP, PROXY_PORT)
    socket.socket = socks.socksocket
    try:
        api.toot(message)
    except Exception as e:
        messageA = '心智模型002号通信ing' + '\n' + '向Mastodon推送消息失败，错误信息为:' + '\n' + str(e)
        CacheHandle.nowMassageId = 'mastodonError'
        MessagePush.messagePush(messageA)
        messageB = '心智模型002号通信ing' + '\n' + '正在尝试重新推送'
        CacheHandle.nowMassageId = 'mastodonError'
        MessagePush.messagePush(messageB)
        messageC = '心智模型002号通信ing' + '\n' + '推送成功，信息已同步至Mastodon'
        try:
            api.toot(message)
            CacheHandle.nowMassageId = 'mastodonError'
            MessagePush.messagePush(messageC)
        except:
            try:
                api.toot(message)
                CacheHandle.nowMassageId = 'mastodonError'
                MessagePush.messagePush(messageC)
            except:
                try:
                    api.toot(message)
                    CacheHandle.nowMassageId = 'mastodonError'
                    MessagePush.messagePush(messageC)
                except:
                    messageD = '心智模型002号通信ing' + '\n' + '错误次数过多，已放弃，请联系节点管理员'
                    CacheHandle.nowMassageId = 'mastodonError'
                    MessagePush.messagePush(messageD)
    socks.setdefaultproxy(socksDefault)
    socket.socket = socketDefault
