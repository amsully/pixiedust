from .SimpleDisplay import SimpleDisplay
from ..display import *
import pixiedust.utils.dataFrameMisc as dataFrameMisc

@PixiedustDisplay()
class SimpleDisplayMeta(DisplayHandlerMeta):

    @addId
    def getMenuInfo(self, entity, dataHandler):
        if(dataFrameMisc.isPySparkDataFrame(entity) or dataFrameMisc.isPandasDataFrame(entity)):
            return [
                {"categoryId": "Table", "title": "Simple Table", "icon": "fa-table", "id": "simpleTest"}
            ]
        else:
            return []

    def newDisplayHandler(self,options,entity):
        return SimpleDisplay(options, entity)