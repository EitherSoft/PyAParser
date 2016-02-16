# -*- coding: utf-8 -*-

# http://a-parser.com/wiki/user-api/

import json
import urllib2
import time


class AParser:
    """
    ping                        - ping
    info                        - info
    one_request                 - oneRequest
    bulk_request                - bulkRequest
    get_parser_preset           - getParserPreset
    get_proxies                 - getProxies
    set_proxy_checker_preset    - setProxyCheckerPreset
    add_task                    - addTask
    get_task_state              - getTaskState
    get_task_conf               - getTaskConf
    get_task_result_file        - getTaskResultsFile
    delete_task_result_file     - deleteTaskResultsFile
    change_task_status          - changeTaskStatus
    move_task                   - moveTask
    get_tasks_list              - getTasksList
    get_parser_info             - getParserInfo
    """
    api_url = None
    password = None

    def __init__(self, api_url, password):
        self.api_url = api_url
        self.password = password

    def _do_request(self, action, data=None, opts=None):
        request = {
          "password": self.password,
          "action": action
        }

        if isinstance(data, dict):
            if isinstance(opts, dict):
                data = dict(data.items() + opts.items())
            request['data'] = data

        req = urllib2.Request(
            self.api_url,
            json.dumps(request),
            {"Content-Type": "text/plain; charset=UTF-8"}
        )
        response = urllib2.urlopen(req).read()
        r = json.loads(response)
        if r['success']:
            return r['data']
        else:
            return False

    def ping(self):
        return self._do_request('ping')

    def info(self):
        return self._do_request('info')

    def get_parser_info(self, parser):
        data = {
            'parser': parser,
        }

        return self._do_request('getParserInfo', data)

    def get_proxies(self):
        return self._do_request('getProxies')

    def get_parser_preset(self, parser, preset):
        data = {
            'parser': parser,
            'preset': preset,
        }

        return self._do_request('getParserPreset', data)

    def one_request(self, parser, preset, query, **kwargs):
        data = {
            'parser': parser,
            'preset': preset,
            'query': query
        }

        return self._do_request('oneRequest', data, kwargs)

    def bulk_request(self, parser, preset, threads, queries, **kwargs):
        data = {
            'parser': parser,
            'preset': preset,
            'queries': queries,
            'threads': threads
        }

        return self._do_request('bulkRequest', data, kwargs)

    def add_task(self, config_preset, preset, queries_from, queries, **kwargs):
        data = {
            'configPreset': config_preset,
            'preset': preset,
            'queriesFrom': queries_from,
            'queries' if queries_from == 'text' else 'queriesFile': queries,
        }

        return self._do_request('addTask', data, kwargs)

    def get_tasks_list(self, completed=0):
        data = {
            'completed': completed
        }

        return self._do_request('getTasksList', data)

    def get_task_state(self, task_id):
        data = {
            'taskUid': task_id,
        }

        return self._do_request('getTaskState', data)

    def get_task_conf(self, task_id):
        data = {
            'taskUid': task_id,
        }

        return self._do_request('getTaskConf', data)

    def change_task_status(self, task_id, to_status):
        # starting|pausing|stopping|deleting
        data = {
            'taskUid': task_id,
            'toStatus': to_status
        }

        return self._do_request('getTaskState', data)

    def move_task(self, task_id, direction):
        # start|end|up|down
        data = {
            'taskUid': task_id,
            'direction': direction
        }

        return self._do_request('moveTask', data)

    def set_proxy_checker_preset(self, preset):
        data = {
            'preset': preset
        }

        return self._do_request('setProxyCheckerPreset', data)

    def get_task_result_file(self, task_id):
        data = {
            'taskUid': task_id
        }

        return self._do_request('getTaskResultsFile', data)

    def delete_task_result_file(self, task_id):
        data = {
            'taskUid': task_id
        }

        return self._do_request('getTaskResultsFile', data)

    def wait_for_task(self, task_id, interval=5):
        while True:
            state = self.get_task_state(task_id)

            if not state or state['status'] == 'completed':
                return state
            time.sleep(interval)
