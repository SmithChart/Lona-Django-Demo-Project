from lona.html import Widget, Div, Ul, Li, A, CLICK


class TabPane(Widget):
    def __init__(self, title, node, active=False):
        self.title = title
        self.node = node
        self.active = active


class Tabs(Widget):
    def __init__(self, *tab_panes):
        self.nodes = [
            Div(
                Ul(_class='nav nav-tabs', role='tablist'),
                Div(_class='tab-content'),
            )
        ]

        for tab_pane in tab_panes:
            if not isinstance(tab_pane, TabPane):
                raise ValueError('unsupported type: {}'.format(type(tab_pane)))

            tab_id = tab_pane.title.lower().replace(' ', '-')

            li = Li(
                A(
                    tab_pane.title,
                    style={
                        'cursor': 'pointer',
                        'margin-right': '20px',
                    },
                    events=[CLICK],
                ),
                _id=tab_id,
                role='tab',
            )

            tab = Div(
                tab_pane.node,
                _id=tab_id,
                _class='tab-pane',
                role='tabpanel',
            )

            if tab_pane.active:
                li.class_list.add('active')
                tab.class_list.add('active')

            self.nodes[0][0].append(li)
            self.nodes[0][1].append(tab)

    def handle_input_event(self, input_event):
        if(input_event.node and
           input_event.node.parent and
           input_event.node.parent.attributes.get('role', '') == 'tab'):

            tab_id = list(input_event.node.parent.id_list)[0]

            for li in self.nodes[0][0]:
                if tab_id in list(li.id_list):
                    li.class_list.add('active')

                else:
                    li.class_list.remove('active')

            for tab in self.nodes[0][1]:
                if tab_id in list(tab.id_list):
                    tab.class_list.add('active')

                else:
                    tab.class_list.remove('active')

            return

        return input_event
