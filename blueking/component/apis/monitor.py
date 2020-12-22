# -*- coding: utf-8 -*-
from ..base import ComponentAPI


class CollectionsMONITOR(object):
    """Collections of MONITOR APIS"""

    def __init__(self, client):
        self.client = client

        self.alarm_instance = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/alarm_instance/',
            description=u'返回指定id的告警数据'
        )

        self.component_instance = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/component_instance/',
            description=u'返回指定id的组件实例'
        )

        self.deploy_script_collector = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/monitor/deploy_script_collector/',
            description=u'脚本采集器任务下发'
        )

        self.export_alarm_strategy = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/export_alarm_strategy/',
            description=u'监控策略导出接口'
        )

        self.export_log_collector = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/export_log_collector/',
            description=u'日志采集器配置导出'
        )

        self.export_script_collector = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/export_script_collector/',
            description=u'脚本采集器配置导出'
        )

        self.export_uptime_check_task = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/export_uptime_check_task/',
            description=u'拨测任务配置导出'
        )

        self.get_alarms = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/get_alarms/',
            description=u'通过筛选条件获取指定告警事件'
        )

        self.get_alarm_strategy = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/get_alarm_strategy/',
            description=u'查询监控策略详情'
        )

        self.get_ts_data = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/monitor/get_ts_data/',
            description=u'图表数据查询'
        )

        self.import_alarm_strategy = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/monitor/import_alarm_strategy/',
            description=u'监控策略入接口'
        )

        self.import_log_collector = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/monitor/import_log_collector/',
            description=u'日志采集器配置导入下发接口'
        )

        self.import_script_collector = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/monitor/import_script_collector/',
            description=u'脚本采集器配置导入'
        )

        self.import_uptime_check_node = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/monitor/import_uptime_check_node/',
            description=u'导入拨测节点'
        )

        self.import_uptime_check_task = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/monitor/import_uptime_check_task/',
            description=u'导入拨测任务'
        )

        self.list_alarm_instance = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/list_alarm_instance/',
            description=u'批量筛选告警'
        )

        self.list_component_instance = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/list_component_instance/',
            description=u'批量筛选组件'
        )

        self.query_data = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/monitor/query_data/',
            description=u'图表数据查询'
        )

        self.metadata_create_data_id = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/monitor/metadata_create_data_id/',
            description=u'创建监控数据源'
        )

        self.metadata_create_result_table = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/monitor/metadata_create_result_table/',
            description=u'创建监控结果表'
        )

        self.metadata_get_data_id = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/metadata_get_data_id/',
            description=u'获取监控数据源具体信息'
        )

        self.metadata_get_result_table = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/metadata_get_result_table/',
            description=u'获取监控结果表具体信息'
        )

        self.metadata_list_result_table = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/metadata_list_result_table/',
            description=u'查询监控结果表'
        )

        self.metadata_modify_result_table = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/metadata_modify_result_table/',
            description=u'修改监控结果表'
        )

        self.save_alarm_strategy = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/monitor/save_alarm_strategy/',
            description=u'保存监控策略'
        )