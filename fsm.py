from transitions.extensions import GraphMachine

from utils import send_text_message,send_image_url,send_button_message,send_normal_message

web_button = [
    {
        "type":"web_url",
        "url":"https://pokemongolive.com/zh_hant/",
        "title":"Pokemon GO"
    }
]
button = [
    {
        "type":"postback",
        "title":"返回",
        "payload":"quit"
    },
    {
        "type":"postback",
        "title":"關於",
        "payload":"about"
    },
    {
        "type":"web_url",
        "url":"https://pokemon.gameinfo.io/zh-tw",
        "title":"View More"
    }
]
btn = [
    {
       "type":"postback",
        "title":"急凍鳥",
        "payload":"pokemon1" 
    },
    {
       "type":"postback",
        "title":"閃電鳥",
        "payload":"pokemon2" 
    },
    {
       "type":"postback",
        "title":"火焰鳥",
        "payload":"pokemon3" 
    },
]
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_official(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'website'
        return False

    def is_going_to_pokedex(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'pokedex'
        elif event.get('postback'):
            text = event['postback']['payload']
            return text.lower() == 'quit'
        return False
    def is_going_to_raid(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'raid'
        return False
    def is_going_to_type(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'type'
        return False
    def is_going_to_mission(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'mission'
        return False
    def is_going_to_pokemon1(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'pokemon1'
        return False
    def is_going_to_pokemon2(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'pokemon2'
        return False
    def is_going_to_pokemon3(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'pokemon3'
        return False

    def is_going_to_pokedscp(self, event):
        if event.get("postback"):
            text = event['postback']['payload']
            return text.lower() == 'about'
        return False

    def on_enter_official(self, event):
        print("I'm entering official")

        sender_id = event['sender']['id']
        send_button_message(sender_id, "官方網站", web_button)
        self.go_back()

    def on_exit_official(self):
        print('Leaving official')

    def on_enter_pokedex(self, event):
        print("I'm entering pokedex")

        sender_id = event['sender']['id']
        send_button_message(sender_id, "Choose the following pokemons:",btn)

    def on_enter_raid(self, event):
        print("I'm entering raid")

        sender_id = event['sender']['id']
        responese = send_image_url(sender_id, "https://truth.bahamut.com.tw/s01/201811/39f895a946ee2dd322464259c55c6c09.JPG")
        self.go_back()

    def on_exit_raid(self):
        print('Leaving raid')
    def on_enter_type(self, event):
        print("I'm entering type")

        sender_id = event['sender']['id']
        responese = send_image_url(sender_id, "https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/48365433_2926339817391522_3004298966075441152_n.jpg?_nc_cat=101&_nc_ht=scontent-tpe1-1.xx&oh=33e6914b47db864ed8c7038b28a13327&oe=5C8D9F2F")
        self.go_back()

    def on_exit_type(self):
        print('Leaving type')
    def on_enter_mission(self, event):
        print("I'm entering mission")

        sender_id = event['sender']['id']
        responese = send_image_url(sender_id, "https://img.4gamers.com.tw/ckfinder/image2/auto/2018-12/47322757_2009211909165691_3977552200460140544_o-181204-192255.jpg?versionId=CVsWBY4cYJnX40Wj3HhEaNDwYGxRc9Zv")
        self.go_back()

    def on_exit_mission(self):
        print('Leaving mission')
    def on_enter_pokemon1(self, event):
        print("I'm entering pokemon1")

        sender_id = event['sender']['id']
        send_normal_message(sender_id, "急凍鳥","冰、飛行","https://pokemon.gameinfo.io/images/pokemon-go/webp/144-00.webp",button)

    def on_enter_pokemon2(self, event):
        print("I'm entering pokemon2")

        sender_id = event['sender']['id']
        send_normal_message(sender_id, "閃電鳥","電、飛行","https://pokemon.gameinfo.io/images/pokemon-go/webp/145-00.webp",button)

    def on_enter_pokemon3(self, event):
        print("I'm entering pokemon3")

        sender_id = event['sender']['id']
        send_normal_message(sender_id, "火焰鳥","火、飛行","https://pokemon.gameinfo.io/images/pokemon-go/webp/146-00.webp",button)

    def on_enter_poke1dscp(self, event):
        print("I'm entering poke1dscp")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "操縱冰的傳說的鳥寶可夢。因為拍動翅膀就能冷卻空氣，所以據說急凍鳥飛過的地方就會下雪。")
        send_text_message(sender_id, "最佳技能組:冰息、冰凍光束")
        self.go_back()
    def on_exit_poke1dscp(self):
        print('Leaving poke1dscp')
    def on_enter_poke2dscp(self, event):
        print("I'm entering poke2dscp")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "操縱電的傳說的鳥寶可夢。平時生活在雷雲之中。被雷電擊中時體內會湧現出力量。")
        send_text_message(sender_id, "最佳技能組:電擊、十萬伏特")
        self.go_back()
    def on_exit_poke2dscp(self):
        print('Leaving poke2dscp')
    def on_enter_poke3dscp(self, event):
        print("I'm entering poke3dscp")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "操縱火的傳說的鳥寶可夢。據說受傷時會鑽進火山口的熔岩裡，燃燒全身來治癒身上的傷口。")
        send_text_message(sender_id, "最佳技能組:火焰炫渦、神鳥猛擊")
        self.go_back()
    def on_exit_poke3dscp(self):
        print('Leaving poke3dscp')
