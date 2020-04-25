# conding = utf-8
import json
import os
class Handle_json(object):
    file_path = os.path.abspath('cookie.json')
    def load_json(self):
        with open(Handle_json.file_path) as fp:
            data = json.load(fp)
            #print(data)
        return data
    def get_data(self):
        return self.load_json()

    def write_cookie(self,data):
        with open(Handle_json.file_path,'w') as fp:
            fp.write(json.dumps(data))


# if __name__ == '__main__':
#
#     data = handle_json.get_data()
#     print(data)
handle_json = Handle_json()