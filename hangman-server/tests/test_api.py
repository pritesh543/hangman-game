from server import app
import unittest
from unittest import TestCase
import json
import sys
import hangman


# Monkey patch the create game function so we can have a deterministic word to test with. This should
# probably read the words from some config and not rely on hardcoded vars but this is simpler.
original_hangman_create = hangman.create_hangman_game


def create_game_with_override_words(words=None, guess_limit=5):
    return original_hangman_create(words=["abac"], guess_limit=5)


hangman.create_hangman_game = create_game_with_override_words


def parse_response(response):
    return json.loads(response.get_data().decode(sys.getdefaultencoding()))


class TestApiIntegration(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def create_game(self):
        return self.app.post("/api/hangman")

    def get_game(self, game_id):
        return self.app.get(f"/api/hangman/{game_id}")

    def guess_game(self, game_id, payload):
        return self.app.post(f"/api/hangman/{game_id}/guess", data=json.dumps(payload))

    def test_create_game(self):
        response = parse_response(self.create_game())

        self.assertIn('gameId', response)
        self.assertEqual(response['state'], 'IN_PROGESS')
        self.assertEqual(response['revealedWord'], '____')
        self.assertEqual(response['numFailedGuessesRemaining'], 5)
        self.assertEqual(response['score'], 5 * 10)

    def test_get_game(self):
        game_id = parse_response(self.create_game())['gameId']
        
        response = parse_response(self.get_game(game_id))

        self.assertEqual(response['gameId'], game_id)
        self.assertEqual(response['state'], 'IN_PROGESS')
        self.assertEqual(response['revealedWord'], '____')
        self.assertEqual(response['numFailedGuessesRemaining'], 5)
        self.assertEqual(response['score'], 5 * 10)

    def test_guess_game(self):
        game_id = parse_response(self.create_game())['gameId']

        response = parse_response(self.guess_game(game_id, {"letter": " "}))

        self.assertEqual(response['error'], 'Please enter valid character')
                
