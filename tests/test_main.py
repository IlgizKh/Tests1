import unittest
from unittest import TestCase

from main import Unique, Geo, ID, mentors, geo_logs, ids


class TestSummarize(TestCase):
    def test_unique_mentors(self):
        expected = "Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий"
        result = Unique(mentors)
        self.assertEqual(result, expected)

    def test_geo_logs(self):
        expected = [
            {'visit1': ['Москва', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]
        result = Geo(geo_logs)
        self.assertEqual(result, expected)

    def test_ids(self):
        expected = [98, 35, 15, 213, 54, 119]
        result = ID(ids)
        self.assertEqual(result, expected)