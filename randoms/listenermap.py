# Description:
# Create a map that allows for listeners to be attached
# and whenever a value is changed, all the callbacks will be run

# put(String key, value);
# addListener(String key, cb);


class my_dict:
    def __init__(self):
        self._d = {}
        self._to_add = {}

    # key = "bob"
    # values = ("value", []) or ("value", ["func"])
    def addListener(self, key, cb):
        if key in self._d:
            self._d[key] = (self._d[key][0], self._d[key][1].append(cb))
        else:
            if key in self._to_add:
                self._to_add[key] = self._to_add[key].append(cb)
            else:
                self._to_add[key] = [cb]

    def put(self, key, value):
        old = None
        if key in self._d:
            old = self._d[key][0]
            self._d[key] = (value, self._d[key][1])
        else:
            if key in self.to_add:
                self._d[key] = (value, self._to_add[key])
                self._to_add.remove(key)
            else:
                self._d[key] = (value, [])

        if old != self._d[key][0]:
            for cb in self._d[key][1]:
                cb()

    def multiPut(self, kvs):
        old = []

        for kv in kvs:
            if kv[0] in self._d:
                old.append(self._d[kv[0]][0])
                self._d[kv[0]] = (kv[1], self._d[kv[0]][1])
            else:
                old.append(None)
                if kv[0] in self.to_add:
                    self._d[kv[0]] = (kv[1], self._to_add[kv[0]])
                    self._to_add.remove(kv[0])
                else:
                    self._d[kv[0]] = (kv[1], [])

        for i in range(len(old)):
            if old[i] != kvs[i][1]:
                for cb in self._d[kvs[i][0]]:
                    cb()
