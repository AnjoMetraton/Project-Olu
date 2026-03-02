import requests
import sys
import os

PELLA_URL = "https://olivinechimpanzee.onpella.app"

s = requests.Session()
usuario_logado = {"nickname": None, "gmail": None}

STRINGS = {
    "pt": {
        "title": "PROJECT OLU",
        "logged_as": "Logado: ",
        "server": "Servidor: ",
        "language_prompt": "Escolha sua linguagem:",
        "language_options": ["[1] Portugues (PT-BR)", "[2] English", "[3] Espanol"],
        "option": "\nOpcao: ",
        "invalid_option": "[!] Opcao invalida.",
        "type_number": "[!] Digite um numero.",
        "login_title": "Login",
        "email": "Gmail: ",
        "password": "Senha: ",
        "logged_ok": "[+] Logado como: ",
        "press_enter": "\n[Enter] para continuar...",
        "error": "[!] Erro: ",
        "no_response": "Sem resposta",
        "connection_error": "[!] Erro de conexao: ",
        "available_chats": "\nChats disponiveis:\n",
        "cancel": "  [0] Cancelar",
        "select_chat": "\nSelecione o {}: ",
        "no_chats": "[!] Nenhum chat encontrado.",
        "chat_type_prompt": "\nTipo de lista de chats:",
        "chat_type_admin": "  [1] Chats em que sou administrador ou co-administrador",
        "chat_type_all": "  [2] Todos os chats ativos",
        "error_list_chats": "[!] Erro ao listar chats: ",
        "error_list_admin": "[!] Erro ao listar chats admin: ",
        "enter_call_title": "Entrar na Call sem Permissao",
        "loading_active_chats": "[*] Carregando chats ativos...",
        "entering_call": "[*] Entrando na call do chat: ",
        "enter_call_ok": "[+] Entrou na call com sucesso!",
        "open_call_title": "Abrir Call",
        "loading_admin_chats": "[*] Carregando chats (admin/co-admin)...",
        "opening_call": "[*] Abrindo call em: ",
        "open_call_ok": "[+] Call aberta com sucesso!",
        "close_call_title": "Fechar Call",
        "closing_call": "[*] Fechando call em: ",
        "close_call_ok": "[+] Call fechada com sucesso!",
        "invite_title": "Convidar Seguidores",
        "selected_chat": "\n[*] Chat selecionado: ",
        "loading_followers": "[*] Carregando seus seguidores...",
        "error_followers": "[!] Erro ao carregar seguidores: ",
        "no_followers": "[!] Nenhum seguidor encontrado.",
        "followers_found": " seguidor(es) encontrado(s).\n",
        "invite_input": "\nNumeros separados por virgula, ou 0 para todos, ou c para cancelar: ",
        "invalid_input": "[!] Entrada invalida.",
        "no_follower_selected": "[!] Nenhum seguidor selecionado.",
        "inviting": "[*] Convidando {} seguidor(es) para {}...",
        "invite_ok": "[+] {} seguidor(es) convidado(s) com sucesso!",
        "transfer_title": "Transferir Administracao",
        "uid_input": "\nUID do novo administrador: ",
        "invalid_uid": "[!] UID invalido.",
        "transferring": "[*] Transferindo administracao de {} para UID {}...",
        "transfer_ok": "[+] Convite de administrador enviado com sucesso para UID {}!",
        "info_title": "Informacoes de Usuario",
        "social_id_input": "Social ID (@usuario): ",
        "invalid_social": "[!] Social ID invalido.",
        "searching": "[*] Buscando @{}...",
        "nickname": "  Nickname:    ",
        "social_id": "  Social ID:   @",
        "uid": "  UID:         ",
        "followers": "  Seguidores:  ",
        "following": "  Seguindo:    ",
        "status": "  Status:      ",
        "online": "  Online:      ",
        "online_yes": "Sim",
        "online_no": "Nao",
        "gender": "  Genero:      ",
        "region": "  Regiao:      ",
        "menu_1": "  [1]  Entrar na call sem permissao",
        "menu_2": "  [2]  Abrir call",
        "menu_3": "  [3]  Fechar call",
        "menu_4": "  [4]  Convidar seguidores para chat",
        "menu_5": "  [5]  Transferir administracao",
        "menu_6": "  [6]  Informacoes de usuario",
        "menu_0": "  [0]  Sair",
        "exiting": "Encerrando Project Olu...",
        "no_title": "Sem titulo",
        "online_tag": " [online]",
        "mutual_tag": " [mutuo]",
    },
    "en": {
        "title": "PROJECT OLU",
        "logged_as": "Logged in: ",
        "server": "Server: ",
        "language_prompt": "Choose your language:",
        "language_options": ["[1] Portugues (PT-BR)", "[2] English", "[3] Espanol"],
        "option": "\nOption: ",
        "invalid_option": "[!] Invalid option.",
        "type_number": "[!] Please type a number.",
        "login_title": "Login",
        "email": "Email: ",
        "password": "Password: ",
        "logged_ok": "[+] Logged in as: ",
        "press_enter": "\n[Enter] to continue...",
        "error": "[!] Error: ",
        "no_response": "No response",
        "connection_error": "[!] Connection error: ",
        "available_chats": "\nAvailable chats:\n",
        "cancel": "  [0] Cancel",
        "select_chat": "\nSelect the {}: ",
        "no_chats": "[!] No chats found.",
        "chat_type_prompt": "\nChat list type:",
        "chat_type_admin": "  [1] Chats where I am admin or co-admin",
        "chat_type_all": "  [2] All active chats",
        "error_list_chats": "[!] Error listing chats: ",
        "error_list_admin": "[!] Error listing admin chats: ",
        "enter_call_title": "Join Call Without Permission",
        "loading_active_chats": "[*] Loading active chats...",
        "entering_call": "[*] Joining call in chat: ",
        "enter_call_ok": "[+] Joined the call successfully!",
        "open_call_title": "Open Call",
        "loading_admin_chats": "[*] Loading chats (admin/co-admin)...",
        "opening_call": "[*] Opening call in: ",
        "open_call_ok": "[+] Call opened successfully!",
        "close_call_title": "Close Call",
        "closing_call": "[*] Closing call in: ",
        "close_call_ok": "[+] Call closed successfully!",
        "invite_title": "Invite Followers",
        "selected_chat": "\n[*] Selected chat: ",
        "loading_followers": "[*] Loading your followers...",
        "error_followers": "[!] Error loading followers: ",
        "no_followers": "[!] No followers found.",
        "followers_found": " follower(s) found.\n",
        "invite_input": "\nNumbers separated by comma, 0 for all, or c to cancel: ",
        "invalid_input": "[!] Invalid input.",
        "no_follower_selected": "[!] No followers selected.",
        "inviting": "[*] Inviting {} follower(s) to {}...",
        "invite_ok": "[+] {} follower(s) invited successfully!",
        "transfer_title": "Transfer Administration",
        "uid_input": "\nUID of the new administrator: ",
        "invalid_uid": "[!] Invalid UID.",
        "transferring": "[*] Transferring admin of {} to UID {}...",
        "transfer_ok": "[+] Admin invite sent successfully to UID {}!",
        "info_title": "User Information",
        "social_id_input": "Social ID (@user): ",
        "invalid_social": "[!] Invalid Social ID.",
        "searching": "[*] Searching @{}...",
        "nickname": "  Nickname:    ",
        "social_id": "  Social ID:   @",
        "uid": "  UID:         ",
        "followers": "  Followers:   ",
        "following": "  Following:   ",
        "status": "  Status:      ",
        "online": "  Online:      ",
        "online_yes": "Yes",
        "online_no": "No",
        "gender": "  Gender:      ",
        "region": "  Region:      ",
        "menu_1": "  [1]  Join call without permission",
        "menu_2": "  [2]  Open call",
        "menu_3": "  [3]  Close call",
        "menu_4": "  [4]  Invite followers to chat",
        "menu_5": "  [5]  Transfer administration",
        "menu_6": "  [6]  User information",
        "menu_0": "  [0]  Exit",
        "exiting": "Exiting Project Olu...",
        "no_title": "No title",
        "online_tag": " [online]",
        "mutual_tag": " [mutual]",
    },
    "es": {
        "title": "PROJECT OLU",
        "logged_as": "Conectado: ",
        "server": "Servidor: ",
        "language_prompt": "Elige tu idioma:",
        "language_options": ["[1] Portugues (PT-BR)", "[2] English", "[3] Espanol"],
        "option": "\nOpcion: ",
        "invalid_option": "[!] Opcion invalida.",
        "type_number": "[!] Escribe un numero.",
        "login_title": "Iniciar Sesion",
        "email": "Correo: ",
        "password": "Contrasena: ",
        "logged_ok": "[+] Conectado como: ",
        "press_enter": "\n[Enter] para continuar...",
        "error": "[!] Error: ",
        "no_response": "Sin respuesta",
        "connection_error": "[!] Error de conexion: ",
        "available_chats": "\nChats disponibles:\n",
        "cancel": "  [0] Cancelar",
        "select_chat": "\nSelecciona el {}: ",
        "no_chats": "[!] No se encontraron chats.",
        "chat_type_prompt": "\nTipo de lista de chats:",
        "chat_type_admin": "  [1] Chats donde soy administrador o co-administrador",
        "chat_type_all": "  [2] Todos los chats activos",
        "error_list_chats": "[!] Error al listar chats: ",
        "error_list_admin": "[!] Error al listar chats admin: ",
        "enter_call_title": "Unirse a la Llamada sin Permiso",
        "loading_active_chats": "[*] Cargando chats activos...",
        "entering_call": "[*] Uniendose a la llamada del chat: ",
        "enter_call_ok": "[+] Te uniste a la llamada con exito!",
        "open_call_title": "Abrir Llamada",
        "loading_admin_chats": "[*] Cargando chats (admin/co-admin)...",
        "opening_call": "[*] Abriendo llamada en: ",
        "open_call_ok": "[+] Llamada abierta con exito!",
        "close_call_title": "Cerrar Llamada",
        "closing_call": "[*] Cerrando llamada en: ",
        "close_call_ok": "[+] Llamada cerrada con exito!",
        "invite_title": "Invitar Seguidores",
        "selected_chat": "\n[*] Chat seleccionado: ",
        "loading_followers": "[*] Cargando tus seguidores...",
        "error_followers": "[!] Error al cargar seguidores: ",
        "no_followers": "[!] No se encontraron seguidores.",
        "followers_found": " seguidor(es) encontrado(s).\n",
        "invite_input": "\nNumeros separados por coma, 0 para todos, o c para cancelar: ",
        "invalid_input": "[!] Entrada invalida.",
        "no_follower_selected": "[!] Ningun seguidor seleccionado.",
        "inviting": "[*] Invitando {} seguidor(es) a {}...",
        "invite_ok": "[+] {} seguidor(es) invitado(s) con exito!",
        "transfer_title": "Transferir Administracion",
        "uid_input": "\nUID del nuevo administrador: ",
        "invalid_uid": "[!] UID invalido.",
        "transferring": "[*] Transfiriendo administracion de {} al UID {}...",
        "transfer_ok": "[+] Invitacion de administrador enviada con exito al UID {}!",
        "info_title": "Informacion de Usuario",
        "social_id_input": "Social ID (@usuario): ",
        "invalid_social": "[!] Social ID invalido.",
        "searching": "[*] Buscando @{}...",
        "nickname": "  Nickname:    ",
        "social_id": "  Social ID:   @",
        "uid": "  UID:         ",
        "followers": "  Seguidores:  ",
        "following": "  Siguiendo:   ",
        "status": "  Estado:      ",
        "online": "  En linea:    ",
        "online_yes": "Si",
        "online_no": "No",
        "gender": "  Genero:      ",
        "region": "  Region:      ",
        "menu_1": "  [1]  Unirse a llamada sin permiso",
        "menu_2": "  [2]  Abrir llamada",
        "menu_3": "  [3]  Cerrar llamada",
        "menu_4": "  [4]  Invitar seguidores al chat",
        "menu_5": "  [5]  Transferir administracion",
        "menu_6": "  [6]  Informacion de usuario",
        "menu_0": "  [0]  Salir",
        "exiting": "Cerrando Project Olu...",
        "no_title": "Sin titulo",
        "online_tag": " [online]",
        "mutual_tag": " [mutuo]",
    }
}

lang = "pt"

def t(key, *args):
    val = STRINGS[lang].get(key, key)
    if args:
        return val.format(*args)
    return val

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho():
    print("=" * 50)
    print(f"          {t('title')}")
    if usuario_logado["nickname"]:
        print(f"       {t('logged_as')}{usuario_logado['nickname']}")
    print("=" * 50)

def input_opcao(max_val):
    try:
        v = int(input(t("option")).strip())
        if 0 <= v <= max_val:
            return v
        print(t("invalid_option"))
        return None
    except ValueError:
        print(t("type_number"))
        return None

def req(endpoint, body=None):
    try:
        r = s.post(f"{PELLA_URL}{endpoint}", json=body or {}, timeout=30)
        return r.status_code, r.json()
    except Exception as e:
        print(f"{t('connection_error')}{e}")
        return None, None

def selecionar_idioma():
    global lang
    cls()
    print("=" * 50)
    print(f"          PROJECT OLU")
    print("=" * 50)
    print()
    print("  Escolha sua linguagem / Choose your language / Elige tu idioma:")
    print()
    for opt in STRINGS["pt"]["language_options"]:
        print(f"  {opt}")
    print()
    try:
        v = int(input("  > ").strip())
        if v == 1:
            lang = "pt"
        elif v == 2:
            lang = "en"
        elif v == 3:
            lang = "es"
        else:
            lang = "pt"
    except ValueError:
        lang = "pt"

def login():
    cls()
    cabecalho()
    print(f"\n  {t('login_title')}\n")
    gmail = input(t("email")).strip()
    senha = input(t("password")).strip()
    status, data = req("/login", {"gmail": gmail, "senha": senha})
    if status == 200:
        nick = data.get("sessionNickname") or data.get("userProfile", {}).get("nickname", "N/A")
        usuario_logado["nickname"] = nick
        usuario_logado["gmail"] = gmail
        print(f"\n{t('logged_ok')}{nick}")
        input(t("press_enter"))
        return True
    else:
        print(f"\n{t('error')}{data.get('error') if data else t('no_response')}")
        input(t("press_enter"))
        return False

def selecionar_chat(chats, label="chat"):
    if not chats:
        print(t("no_chats"))
        return None
    print(t("available_chats"))
    for i, c in enumerate(chats):
        titulo = c.get("title", t("no_title"))
        tid = c.get("thread_id", "")
        cargo = c.get("cargo", "")
        extra = f" [{cargo}]" if cargo else ""
        print(f"  [{i+1}] {titulo}{extra}  ({tid})")
    print(t("cancel"))
    try:
        op = int(input(t("select_chat").format(label)).strip())
        if op == 0:
            return None
        if 1 <= op <= len(chats):
            return chats[op - 1]
        print(t("invalid_option"))
        return None
    except ValueError:
        print(t("type_number"))
        return None

def obter_chats_normais():
    status, data = req("/listar-chats")
    if status == 200 and isinstance(data, list):
        return data
    print(f"{t('error_list_chats')}{data.get('error') if data else t('no_response')}")
    return []

def obter_chats_admin():
    status, data = req("/chats-admin")
    if status == 200 and isinstance(data, list):
        return data
    print(f"{t('error_list_admin')}{data.get('error') if data else t('no_response')}")
    return []

def escolher_tipo_chat():
    print(t("chat_type_prompt"))
    print(t("chat_type_admin"))
    print(t("chat_type_all"))
    print(t("cancel"))
    op = input_opcao(2)
    if op == 1:
        return obter_chats_admin()
    elif op == 2:
        return obter_chats_normais()
    return []

def entrar_call_sem_permissao():
    cls()
    cabecalho()
    print(f"\n  {t('enter_call_title')}\n")
    print(t("loading_active_chats"))
    chats = obter_chats_normais()
    chat = selecionar_chat(chats)
    if not chat:
        return
    tid = chat.get("thread_id")
    print(f"\n{t('entering_call')}{chat.get('title')}...")
    status, data = req("/entrar-na-call", {"thread_id": tid})
    if status == 200:
        print(t("enter_call_ok"))
    else:
        print(f"{t('error')}{data.get('error') if data else t('no_response')}")
    input(t("press_enter"))

def abrir_call():
    cls()
    cabecalho()
    print(f"\n  {t('open_call_title')}\n")
    print(t("loading_admin_chats"))
    chats = obter_chats_admin()
    chat = selecionar_chat(chats)
    if not chat:
        return
    tid = chat.get("thread_id")
    print(f"\n{t('opening_call')}{chat.get('title')}...")
    status, data = req("/abrir-a-call", {"thread_id": tid})
    if status == 200 and data.get("success"):
        print(t("open_call_ok"))
    else:
        print(f"{t('error')}{data.get('error') if data else t('no_response')}")
    input(t("press_enter"))

def fechar_call():
    cls()
    cabecalho()
    print(f"\n  {t('close_call_title')}\n")
    print(t("loading_admin_chats"))
    chats = obter_chats_admin()
    chat = selecionar_chat(chats)
    if not chat:
        return
    tid = chat.get("thread_id")
    print(f"\n{t('closing_call')}{chat.get('title')}...")
    status, data = req("/fechar-a-call", {"thread_id": tid})
    if status == 200 and data.get("success"):
        print(t("close_call_ok"))
    else:
        print(f"{t('error')}{data.get('error') if data else t('no_response')}")
    input(t("press_enter"))

def convidar_seguidores():
    cls()
    cabecalho()
    print(f"\n  {t('invite_title')}\n")
    chats = escolher_tipo_chat()
    chat = selecionar_chat(chats)
    if not chat:
        return
    tid = chat.get("thread_id")
    print(f"{t('selected_chat')}{chat.get('title')}")
    print(t("loading_followers"))
    status, data = req("/meus-seguidores", {})
    if status != 200 or not data.get("success"):
        print(f"{t('error_followers')}{data.get('error') if data else t('no_response')}")
        input(t("press_enter"))
        return
    seguidores = data.get("seguidores", [])
    if not seguidores:
        print(t("no_followers"))
        input(t("press_enter"))
        return
    print(f"\n{len(seguidores)}{t('followers_found')}")
    for i, seg in enumerate(seguidores):
        nick = seg.get("nickname", "N/A")
        sid = seg.get("social_id", "")
        online = t("online_tag") if seg.get("online_status") == 1 else ""
        mutuo = t("mutual_tag") if seg.get("follow_me_status") == 1 and seg.get("followed_by_me_status") == 1 else ""
        print(f"  [{i+1}] {nick} @{sid}{online}{mutuo}")
    escolha = input(t("invite_input")).strip()
    if escolha.lower() == 'c':
        return
    uids = []
    if escolha == '0':
        uids = [seg.get("uid") for seg in seguidores]
    else:
        try:
            indices = [int(x.strip()) - 1 for x in escolha.split(',')]
            uids = [seguidores[i].get("uid") for i in indices if 0 <= i < len(seguidores)]
        except ValueError:
            print(t("invalid_input"))
            input(t("press_enter"))
            return
    if not uids:
        print(t("no_follower_selected"))
        input(t("press_enter"))
        return
    print(f"\n{t('inviting', len(uids), chat.get('title'))}")
    status, data = req("/convidar-usuarios", {"thread_id": tid, "uids": uids})
    if status == 200 and data.get("success"):
        print(t("invite_ok", len(uids)))
    else:
        print(f"{t('error')}{data.get('error') if data else t('no_response')}")
    input(t("press_enter"))

def transferir_admin():
    cls()
    cabecalho()
    print(f"\n  {t('transfer_title')}\n")
    print(t("loading_admin_chats"))
    chats = obter_chats_admin()
    chat = selecionar_chat(chats)
    if not chat:
        return
    tid = chat.get("thread_id")
    uid = input(t("uid_input")).strip()
    if not uid:
        print(t("invalid_uid"))
        return
    print(f"\n{t('transferring', chat.get('title'), uid)}")
    status, data = req("/transferir-admin", {"thread_id": tid, "uid": uid})
    if status == 200 and data.get("success"):
        print(t("transfer_ok", uid))
    else:
        print(f"{t('error')}{data.get('error') if data else t('no_response')}")
    input(t("press_enter"))

def info_usuario():
    cls()
    cabecalho()
    print(f"\n  {t('info_title')}\n")
    social_id = input(t("social_id_input")).strip().lstrip('@')
    if not social_id:
        print(t("invalid_social"))
        return
    print(f"\n{t('searching', social_id)}")
    status, data = req("/info-usuario", {"social_id": social_id})
    if status == 200 and data.get("success"):
        u = data.get("data", {}).get("data", data.get("data", {}))
        print(f"\n{t('nickname')}{u.get('nickname', 'N/A')}")
        print(f"{t('social_id')}{u.get('socialId', 'N/A')}")
        print(f"{t('uid')}{u.get('uid', 'N/A')}")
        print(f"{t('followers')}{u.get('fansCount', 'N/A')}")
        print(f"{t('following')}{u.get('followingCount', 'N/A')}")
        print(f"{t('status')}{u.get('status', 'N/A')}")
        print(f"{t('online')}{t('online_yes') if u.get('onlineStatus') == 1 else t('online_no')}")
        print(f"{t('gender')}{u.get('gender', 'N/A')}")
        print(f"{t('region')}{u.get('contentRegionName', 'N/A')}")
    else:
        print(f"{t('error')}{data.get('error') if data else t('no_response')}")
    input(t("press_enter"))

def menu_principal():
    while True:
        cls()
        cabecalho()
        print()
        print(t("menu_1"))
        print(t("menu_2"))
        print(t("menu_3"))
        print(t("menu_4"))
        print(t("menu_5"))
        print(t("menu_6"))
        print(t("menu_0"))
        print()
        op = input_opcao(6)
        if op is None:
            continue
        if op == 1:
            entrar_call_sem_permissao()
        elif op == 2:
            abrir_call()
        elif op == 3:
            fechar_call()
        elif op == 4:
            convidar_seguidores()
        elif op == 5:
            transferir_admin()
        elif op == 6:
            info_usuario()
        elif op == 0:
            cls()
            print(t("exiting"))
            sys.exit(0)

if __name__ == "__main__":
    selecionar_idioma()
    cls()
    cabecalho()
    print(f"\n  {t('server')}{PELLA_URL}\n")
    if not login():
        sys.exit(1)
    menu_principal()
