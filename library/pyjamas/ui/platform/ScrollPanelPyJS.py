class ScrollPanel(SimplePanel):

    def ensureVisibleImpl(self, scroll, e):
        JS("""
        if (!e) return;

        var item = e;
        var realOffset = 0;
        while (item && (item != scroll)) {
            realOffset += item.offsetTop;
            item = item.offsetParent;
            }

        scroll.scrollTop = realOffset - scroll.offsetHeight / 2;
        """)


