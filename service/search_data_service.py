from dao.load_data import *


def load_all_bookmarks():
    bookmarks = load_data()
    return bookmarks


bookmarks = load_all_bookmarks()


def load_bookmarks_by_id(id1):
    for bookmark in bookmarks:
        if bookmark["id"] == id1:
            return bookmark


def get_bookmark_index_for_id(id):
    index = 0
    for bk in bookmarks:
        if bk['id'] == id:
            return index
        index += 1
    return -1


def check_If_bookmark_exist(bookmark):
    bkm = load_bookmarks_by_id(bookmark['id'])
    print('check_If_bookmark_exist', end='')
    print(bkm)
    if bkm is None:
        return 0
    return 1


def add_bookmarks(bookmark):
    exist = check_If_bookmark_exist(bookmark)
    if exist == 0:
        bookmarks.append(bookmark)
        print('In service::')
        print(bookmarks)
        load_bookmarks(bookmarks)
        return 'Bookmark created successfully'
    return 'Bookmark already exist'


def modify_bookmarks(data, id):
    bookmark = load_bookmarks_by_id(id)

    if bookmark is not None:
        bookmark["name"] = data["name"]
        bookmark["category"] = data["category"]
        bookmark["url"] = data["url"]
        load_bookmarks(bookmarks)
        return 'Bookmark updated successfully'

    return 'Bookmark with provided id doesnot exist'


def delete_bookmarks(id):
    index = get_bookmark_index_for_id(id)
    if index != -1:
        bookmarks.pop(index)
        print(bookmarks)
        return "Bookmark removed successfully"
    return "Bookmark with given id not found"
