
class Timer:

    def __setTimeout(self, delayMillis):
        JS("""
        return $wnd.setTimeout(function() { @{{self}}.__fire(); }, @{{delayMillis}});
        """)

    def __clearTimeout(self,tid):
        JS("""
        $wnd.clearTimeout(@{{tid}});
        """)

    def __setInterval(self, periodMillis):
        JS("""
        return $wnd.setInterval(function() { @{{self}}.__fire(); }, @{{periodMillis}});
        """)

    def __clearInterval(self,tid):
        JS("""
        $wnd.clearInterval(@{{tid}});
        """)

