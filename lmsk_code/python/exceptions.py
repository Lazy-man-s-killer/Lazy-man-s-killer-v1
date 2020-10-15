# coding:utf-8
"""
 * @Author 20261
 * @create 2020/10/15 18:40
 * User: 20261
 * Date: 2020/10/15
 * Created by 20261 on 2020/10/15.
 * Use: 
"""

class LMSKException(IOError):
    """There was an ambiguous exception that occurred while handling your
    request.
    """

    def __init__(self, *args, **kwargs):
        super(LMSKException, self).__init__(*args, **kwargs)
