from ..display import *
from pyspark.sql import DataFrame
from pixiedust.utils.dataFrameAdapter import *
import pixiedust.utils.dataFrameMisc as dataFrameMisc

class SimpleDisplay(Display):

    def doRender(self, handlerId):
        entity = self.entity

        if(dataFrameMisc.isPySparkDataFrame(entity) or dataFrameMisc.isPandasDataFrame(entity)):
            self._addHTMLTemplate('simpleTable.html', entity=PandasDataFrameAdapter(entity))
            return

        self._addHTML("""
            <b>Unable to display object!</b>
        """)