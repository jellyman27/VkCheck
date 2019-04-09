import vk_api

print("Авторизация пользователя")
login = input("Введите ваш логин(Номер телефона): ")
password = input("Введите ваш пароль: ")
vk_session = vk_api.VkApi(login, pasword)
vk_session.auth()
vk = vk_session.get_api()
id_group = input("Введите ID группы: ")
id_user = input("Введите ID пользователя или напишите 'STOP' для остановки скрипта: ")
print("ID   Состоит в группе    Лайк    Комментарий")
while id_user != "STOP":
    liked = 0
    iscomments = 0
    endstr = id_user + "  "
    isMember = vk.groups.isMember(group_id = id_group, user_id = id_user)
    endstr += " "+ str(isMember)
    walls = vk.wall.get(domain = id_group, count = 10)
    id_owner = walls["items"].pop()["owner_id"]
    for wall in walls["items"]:
        id_wall = wall["id"]
        isLiked = vk.likes.isLiked(user_id = id_user, type = "post", owner_id = id_owner, item_id = id_wall)
        if isLiked["liked"] == 1:
            liked = 1
        offset = 0
        comments = vk.wall.getComments(owner_id = id_owner, post_id = id_wall, offset = offset, count = 1)
        count = comments["count"]
        while offset < count:
            com = comments["items"]
            try:
                com = com.pop()
                if int(id_user) == int(com["from_id"]):
                    iscomments = 1
            except:
                pass
            offset +=1
            comments = vk.wall.getComments(owner_id = id_owner, post_id = id_wall, offset = offset, count = 1)
            count = comments["count"]
    endstr += "  " + str(liked) + "  " + str(iscomments)
    print(endstr)
    id_user = input("Введите ID пользователя или напишите 'STOP' для остановки скрипта ")

