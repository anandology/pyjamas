
import GChartTestAppUtil
from pyjamas.chart.GChart import GChart


"""* Empty chart without anything on it except a title and footnotes """
class TestGChart00 (GChart):
    def __init__(self):
        GChart.__init__(self, XChartSize=150, YChartSize=150)
        self.setChartTitle(GChartTestAppUtil.getTitle(self))
        self.setChartFootnotes("Check: Consistent with a 'no data' chart (and it doesn't crash).")
    


