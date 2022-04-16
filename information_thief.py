from bs4 import BeautifulSoup
import requests
from models import Tags, Anime, Manga, Type, Status, Genres, Tag_anime, Tag_manga, Genre_anime, Genre_manga
from app import db
import re
from sqlalchemy import insert


def take_url(url_, cls):
    index = []
    limit = 0
    for i in range(1):
        url = f'{url_}{int(limit)}'
        req = requests.get(url)
        src = req.text
        soap = BeautifulSoup(src, 'lxml')
        all_names = soap.find_all(class_=cls)
        for all_a in all_names:
            all_link = all_a.find('a')
            print(all_link['href'])
            index.append(all_link['href'])
        limit += 50
    return index


def insert_inf_tags_genr(inf, SQL):
    k = 0
    for i in inf:
        k += 1
        print(i.text, 'i text')
        filtered_str = i.text.split()
        print(filtered_str, 'fflflfll')
        filtered_str.pop()
        filtered_str = ' '.join(filtered_str)
        filtered_str = filtered_str.strip()
        print(filtered_str)
        abobus = SQL(name=filtered_str)
        db.session.add(abobus)
        db.session.commit()


def thief_tags_and_genres():
    index = 0
    url = f'https://myanimelist.net/manga.php'
    req = requests.get(url)
    src = req.text
    soap = BeautifulSoup(src, 'lxml')
    tagaga = soap.find_all(class_='genre-link')
    for block_tag in tagaga:
        index += 1
        if index < 3:
            all_tags = block_tag.find_all(class_='genre-name-link')
            insert_inf_tags_genr(all_tags, Genres)
        elif index == 3:
            all_tags = block_tag.find_all(class_='genre-name-link')
            insert_inf_tags_genr(all_tags, Tags)
        else:
            break


def create_types():
    type_1 = Type(name='TV')
    db.session.add(type_1)
    type_2 = Type(name='Movie')
    db.session.add(type_2)
    type_3 = Type(name='OVA')
    db.session.add(type_3)
    type_4 = Type(name='ONA')
    db.session.add(type_4)
    type_5 = Type(name='Special')
    db.session.add(type_5)
    type_6 = Type(name='Manga')
    db.session.add(type_6)
    type_7 = Type(name='One-shot')
    db.session.add(type_7)
    type_8 = Type(name='Doujinshi')
    db.session.add(type_8)
    type_9 = Type(name='Light Novel')
    db.session.add(type_9)
    type_10 = Type(name='Novel')
    db.session.add(type_10)
    type_11 = Type(name='Manhwa')
    db.session.add(type_11)
    type_12 = Type(name='Manhua')
    db.session.add(type_12)
    type_13 = Type(name='Music')
    db.session.add(type_13)
    db.session.commit()


def create_status():
    status_1 = Status(name='Finished Airing')
    db.session.add(status_1)
    status_2 = Status(name='Currently Airing')
    db.session.add(status_2)
    status_3 = Status(name='Not yet aired')
    db.session.add(status_3)
    status_4 = Status(name='Finished')
    db.session.add(status_4)
    status_5 = Status(name='Publishing')
    db.session.add(status_5)
    status_6 = Status(name='On Hiatus')
    db.session.add(status_6)
    status_7 = Status(name='Not yet published')
    db.session.add(status_7)
    status_8 = Status(name='Discontinued')
    db.session.add(status_8)
    db.session.commit()


def anime_inf(cls, string):
    for i in cls:
        type = i.find(string=re.compile(string))
        if type != None:
            names = i.text.split()
            names.pop(0)
            name_type = ' '.join(names)
            if name_type == 'Unknown' and string == 'Episodes':
                name_type = 0
                return name_type
            elif string == 'Genre' or string == 'Genres':
                text = i.find_all('a')

                genres = []
                for ff in text:
                    print(ff.text)
                    filter = Genres.query.filter_by(name=ff.text).first()
                    print(filter)
                    genres.append(filter.id)
                return genres
            elif string == 'Themes' or string == 'Theme':
                text = i.find_all('a')
                tags = []
                for ff in text:
                    filter = Tags.query.filter_by(name=ff.text).first()
                    print(ff.text)
                    tags.append(filter.id)
                return tags
            elif string == 'Ranked':
                names = i.text.split()
                names.pop(0)
                name_type = names[0]
                name_second = list(name_type)
                name_second.pop(0)
                name_second.pop()
                name_type_second = ''.join(name_second)
                if name_type_second == 'N/A1':
                    name_type_second = 0
                return name_type_second

            elif string == 'Score':
                names = i.text.split()
                name_type = names[1]
                if name_type == 'N/A1':
                    name_type = 0
                return name_type
            else:
                if string == 'Type':

                    filter = Type.query.filter_by(name=name_type).first()
                    type_for_sql = filter.id
                    return type_for_sql
                elif string == 'Status':
                    filter = Status.query.filter_by(name=name_type).first()
                    type_for_sql = filter.id
                    return type_for_sql

                else:
                    return name_type


def manga_inf(cls, string):
    for i in cls:
        type = i.find(string=re.compile(string))
        if type != None:
            names = i.text.split()
            names.pop(0)
            name_type = ' '.join(names)
            if name_type == 'Unknown' and string == 'Volumes':
                name_type = 0
                return name_type
            elif name_type == 'Unknown' and string == 'Chapters':
                name_type = 0
                return name_type
            elif string == 'Genre' or string == 'Genres':
                text = i.find_all('a')

                genres = []
                for ff in text:
                    filter = Genres.query.filter_by(name=ff.text.strip()).first()

                    genres.append(filter.id)
                return genres
            elif string == 'Themes' or string == 'Theme':
                text = i.find_all('a')
                tags = []
                for ff in text:
                    filter = Tags.query.filter_by(name=ff.text.strip()).first()

                    tags.append(filter.id)
                return tags
            elif string == 'Ranked':
                names = i.text.split()
                names.pop(0)
                name_type = names[0]
                name_second = list(name_type)
                name_second.pop(0)
                name_second.pop()
                name_type_second = ''.join(name_second)
                if name_type_second == 'N/A1':
                    name_type_second = 0
                return name_type_second

            elif string == 'Score':
                names = i.text.split()
                name_type = names[1]
                if name_type == 'N/A1':
                    name_type = 0
                return name_type
            else:
                if string == 'Type':

                    filter = Type.query.filter_by(name=name_type).first()
                    type_for_sql = filter.id
                    return type_for_sql
                elif string == 'Status':
                    filter = Status.query.filter_by(name=name_type).first()
                    type_for_sql = filter.id
                    return type_for_sql

                else:
                    return name_type


def anime_thief(urls):
    for i in urls:
        url = i
        req = requests.get(url)
        src = req.text
        soap = BeautifulSoup(src, 'lxml')
        title = soap.find(class_='title-name h1_bold_none')
        if title != None:
            block_type = soap.find_all(class_='spaceit_pad')

            title_sql = title.text
            print(title_sql)

            all_img = soap.find_all('img', limit=3)
            for rr in all_img:

                if rr['alt'] == title_sql:
                    img = rr['data-src']
                    break
                else:
                    pass
            type = anime_inf(block_type, 'Type')
            episodes = anime_inf(block_type, 'Episodes')
            status = anime_inf(block_type, 'Status')
            genres = anime_inf(block_type, 'Genre')
            tags = anime_inf(block_type, 'Theme')

            ranked = anime_inf(block_type, 'Ranked')
            score = anime_inf(block_type, 'Score')
            alternative_titles = anime_inf(block_type, 'Synonyms')
            sinpopus_block = soap.find('p', attrs={"itemprop": "description"}).text
            if sinpopus_block == None:
                sinpopus_block = 'No sinpopus'

            abobus = Anime(title=title_sql, img=img, type=type, episodes=episodes, status=status, ranked=ranked,
                           score=score, sinpopus=sinpopus_block, alternative_titles=alternative_titles)
            db.session.add(abobus)
            db.session.commit()
            if tags != None:
                for vpopus in tags:
                    abobus_tags = Tag_anime.insert().values(
                        tag_id=vpopus, anime_id=abobus.id
                    )
                    db.session.execute(abobus_tags)
            if genres != None:
                for vjopus in genres:
                    abobus_genr = Genre_anime.insert().values(
                        genr_id=vjopus, anime_id=abobus.id
                    )
                    db.session.execute(abobus_genr)
                db.session.commit()


def manga_thief(urls):

    for i in urls:
        url = i
        req = requests.get(url)
        src = req.text
        soap = BeautifulSoup(src, 'lxml')
        title = soap.find(attrs={"itemprop": "name"})

        if title != None:
            block_type = soap.find_all(class_='spaceit_pad')
            k = 0
            all_img = soap.find_all('img', limit=3)
            for rr in all_img:
                k += 1
                if k == 3:
                    title_sql = rr['alt']
                    print(title_sql)
                    img = rr['data-src']
            type = manga_inf(block_type, 'Type')
            volumes = manga_inf(block_type, 'Volumes')
            chapters = manga_inf(block_type, 'Chapters')
            status = manga_inf(block_type, 'Status')
            genres = manga_inf(block_type, 'Genre')
            tags = manga_inf(block_type, 'Theme')
            ranked = manga_inf(block_type, 'Ranked')
            score = manga_inf(block_type, 'Score')
            alternative_titles = manga_inf(block_type, 'Synonyms')
            sinpopus_block = soap.find('span', attrs={"itemprop": "description"})
            if sinpopus_block is None:
                sinpopus_block = 'No sinpopus'
            else:
                sinpopus_block = sinpopus_block.text
            abobus = Manga(title=title_sql, img=img, type=type, volumes=volumes, chapters=chapters, status=status,
                           ranked=ranked, score=score, sinpopus=sinpopus_block, alternative_titles=alternative_titles)
            print(abobus.title)
            db.session.add(abobus)
            db.session.commit()
            if tags != None:
                for vpopus in tags:
                    abobus_tags = Tag_manga.insert().values(
                        tag_id=vpopus, manga_id=abobus.id
                    )
                    db.session.execute(abobus_tags)
            if genres != None:
                for vjopus in genres:
                    abobus_genr = Genre_manga.insert().values(
                        genr_id=vjopus, manga_id=abobus.id
                    )
                    db.session.execute(abobus_genr)
            db.session.commit()

s = take_url('https://myanimelist.net/topanime.php?type=upcoming&limit=','hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3')
while s.index('https://myanimelist.net/anime/49709/Fumetsu_no_Anata_e_2nd_Season') != 0:
    s.pop(0)
s.pop(0)
print(s)
anime_thief(s)

