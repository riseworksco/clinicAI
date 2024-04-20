from io import BytesIO  # 导入BytesIO以进行类型检查
from unittest.mock import ANY, MagicMock, patch  # 导入ANY

from django.test import SimpleTestCase

from assessment.forms import StompForm


class TestStompForm(SimpleTestCase):
    def setUp(self):
        self.form_data = {
            "TherapistEmail": "therapist@example.com",
            "Alternative": 3,
            "Bluegrass": 2,
            "Blues": 4,
            "Classical": 5,
            "Country": 2,
            "Dance_Electronica": 3,
            "Folk": 2,
            "Funk": 3,
            "Gospel": 2,
            "Heavy_Meta": 3,
            "World": 4,
            "Jazz": 2,
            "New_Age": 3,
            "Oldies": 2,
            "Opera": 3,
            "Pop": 5,
            "Punk": 5,
            "Rap_hip_hop": 5,
            "Reggae": 5,
            "Religious": 5,
            "Rock": 5,
            "Soul_R_B": 5,
            "Soundtracks_heme_song": 5,
        }

    @patch("assessment.forms.EmailMessage")
    def test_send_email_without_database(self, mock_email_message):
        form = StompForm(data=self.form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)

        mock_email = MagicMock()
        mock_email_message.return_value = mock_email

        form.send()

        mock_email.send.assert_called_once()
        mock_email.attach.assert_called_once_with(
            "music_preferences.pdf", ANY, "application/pdf"
        )  # 使用ANY

    @patch("assessment.forms.canvas.Canvas")
    def test_generate_pdf_without_saving_file(self, mock_canvas):
        form = StompForm(data=self.form_data)
        self.assertTrue(form.is_valid(), msg=form.errors)

        form.generate_pdf_file()

        mock_canvas.assert_called_once()
        args, kwargs = mock_canvas.call_args
        self.assertIsInstance(args[0], BytesIO)  # 检查传入的是BytesIO对象
