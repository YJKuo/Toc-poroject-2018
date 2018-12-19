from bottle import route, run, request, abort, static_file

from fsm import TocMachine


VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']
machine = TocMachine(
    states=[
        'user',
        'official',
        'pokedex',
        'raid',
        'type',
        'mission',
        'pokemon1',
        'pokemon2',
        'pokemon3',
        'poke1dscp',
        'poke3dscp',
        'poke2dscp'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'official',
            'conditions': 'is_going_to_official'
        },
        {
            'trigger': 'advance',
            'source': [
                'user',
                'pokemon1',
                'pokemon2',
                'pokemon3'
            ],
            'dest': 'pokedex',
            'conditions': 'is_going_to_pokedex'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'raid',
            'conditions': 'is_going_to_raid'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'type',
            'conditions': 'is_going_to_type'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'mission',
            'conditions': 'is_going_to_mission'
        },
        {
            'trigger': 'advance',
            'source': 'pokedex',
            'dest': 'pokemon1',
            'conditions': 'is_going_to_pokemon1'
        },
        {
            'trigger': 'advance',
            'source': 'pokedex',
            'dest': 'pokemon2',
            'conditions': 'is_going_to_pokemon2'
        },
        {
            'trigger': 'advance',
            'source': 'pokedex',
            'dest': 'pokemon3',
            'conditions': 'is_going_to_pokemon3'
        },
        {
            'trigger': 'advance',
            'source': 'pokemon1',
            'dest': 'poke1dscp',
            'conditions': 'is_going_to_pokedscp'
        },
        {
            'trigger': 'advance',
            'source': 'pokemon2',
            'dest': 'poke2dscp',
            'conditions': 'is_going_to_pokedscp'
        },
        {
            'trigger': 'advance',
            'source': 'pokemon3',
            'dest': 'poke3dscp',
            'conditions': 'is_going_to_pokedscp'
        },
        {
            'trigger': 'go_back',
            'source': [
                'official',
                'raid',
                'type',
                'mission',
                'poke1dscp',
                'poke2dscp',
                'poke3dscp'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
