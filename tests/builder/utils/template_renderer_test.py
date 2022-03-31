from unittest import TestCase, mock
from unittest.mock import Mock

from jinja2 import TemplateSyntaxError

from osbenchmark.builder.utils.template_renderer import TemplateRenderer
from osbenchmark.exceptions import InvalidSyntax, SystemSetupError


class TemplateRendererTest(TestCase):
    def setUp(self):
        self.root_path = "fake"
        self.variables = {}
        self.file_name = "non-existent.txt"
        self.template_renderer = TemplateRenderer()

    @mock.patch('jinja2.Environment.get_template')
    def test_successful_render(self, get_template):
        template = Mock()
        get_template.return_value = template
        template.render.return_value = "template as string"

        self.template_renderer.render_template(self.root_path, self.variables, self.file_name)

    @mock.patch('jinja2.Environment.get_template')
    def test_template_syntax_error(self, get_template):
        get_template.side_effect = TemplateSyntaxError("fake", 12)

        with self.assertRaises(InvalidSyntax):
            self.template_renderer.render_template(self.root_path, self.variables, self.file_name)

    @mock.patch('jinja2.Environment.get_template')
    def test_unknown_error(self, get_template):
        template = Mock()
        get_template.return_value = template
        template.render.side_effect = RuntimeError()

        with self.assertRaises(SystemSetupError):
            self.template_renderer.render_template(self.root_path, self.variables, self.file_name)
