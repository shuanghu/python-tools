# coding:utf-8
import re

js_resource_pattern = re.compile('''.*?(\S*):.*?'(.*)'.*''')


def js_code_format(line):
    pass


def js_format(line):
    match = js_resource_pattern.match(line)
    if match:
        return match.group(1), match.group(2)
    return None


def wiki_js_format(path):
    res_map = {}
    res = ['']
    for line in open(path, "r", encoding='utf-8'):
        kv = js_format(line.replace("\r", "").replace("\n", ""))
        if kv is None:
            continue
        if kv[0] == res[0]:
            if len(res) == 2:
                res_map[kv[0]] = kv[1]
                print(kv)
                res.append(kv[0])
            else:
                continue
        else:
            res = [kv[0], kv[1]]
            print("zh: %s,%s" % kv)
    return res_map


def java_format(line):
    pass


def wiki_2_js(path, res_map):
    target = open("F:\\js_new.js", "w", encoding='utf-8')
    for line in open(path, "r", encoding='utf-8'):
        data = line.replace("\r", "").replace("\n", "")
        kv = js_format(data)
        if kv is None:
            target.write(line)
            continue
        if kv[0] in res_map:
            target.write("  %s: '%s',\n" % (kv[0], res_map[kv[0]].replace("\'", "\\'")))
            continue
        else:
            print(line)
            target.write(line)


def js_i18n(path):
    i18n_res = {}

    for line in open(path, "r", encoding='utf-8'):
        data = line.replace("\r", "").replace("\n", "")
        kv = js_format(data)
        if kv is None:
            continue
        i18n_res[kv[0]] = kv[1]
    return i18n_res


def js_2_wiki(path_zh, path_rude, path_result):
    result = open(path_result, "w", encoding='utf-8')
    zh_i18n = js_i18n(path_zh)
    rude_i18n = js_i18n(path_rude)

    for k, v in zh_i18n.items():
        result.write("%s : %s\n" % (k, v.replace("\\'", "'")))
        if k in rude_i18n:
            result.write("%s : %s\n" % (k, rude_i18n.get(k).replace("\\'", "'")))
        else:
            result.write("%s : %s\n" % (k, ""))
    result.flush()
    result.close()


if __name__ == '__main__':
    # res_map = wiki_js_format("F:\\js.txt")
    # wiki_2_js("F:\\work\\source\\SalliteWeb\\src\\language\\fr-FR.js", res_map)
    js_2_wiki("F:\\work\\source\\SalliteWeb\\src\\language\\zh-CN.js",
              "F:\\work\\source\\SalliteWeb\\src\\language\\fr-FR.js", "F:\\wiki.txt")
