import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from startrax.models import Review, Album  # Use absolute import

@pytest.mark.django_db
def test_homepage_access(client):
    response = client.get(reverse('review_list'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_review(client):
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    album = Album.objects.create(name='Test Album', year=2023, artist='Test Artist', user=user)
    response = client.post(reverse('review_create'), {
        'album': album.id,
        'star_rating': 5,
        'note': 'Great album!'
    })
    assert response.status_code == 302  # Redirect after successful creation
    assert Review.objects.filter(user=user, album=album).exists()

@pytest.mark.django_db
def test_update_review(client):
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    album = Album.objects.create(name='Test Album', year=2023, artist='Test Artist', user=user)
    review = Review.objects.create(user=user, album=album, star_rating=4, note='Good album')
    response = client.post(reverse('review_update', args=[review.id]), {
        'album': album.id,
        'star_rating': 5,
        'note': 'Great album!'
    })
    assert response.status_code == 302  # Redirect after successful update
    review.refresh_from_db()
    assert review.star_rating == 5
    assert review.note == 'Great album!'

@pytest.mark.django_db
def test_delete_review(client):
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    album = Album.objects.create(name='Test Album', year=2023, artist='Test Artist', user=user)
    review = Review.objects.create(user=user, album=album, star_rating=4, note='Good album')
    response = client.post(reverse('review_delete', args=[review.id]))
    assert response.status_code == 302  # Redirect after successful deletion
    assert not Review.objects.filter(id=review.id).exists()

@pytest.mark.django_db
def test_create_album(client):
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    response = client.post(reverse('album_create'), {
        'name': 'Test Album',
        'year': 2023,
        'artist': 'Test Artist'
    })
    assert response.status_code == 302  # Redirect after successful creation
    assert Album.objects.filter(name='Test Album', user=user).exists()


@pytest.mark.django_db
def test_delete_album(client):
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    album = Album.objects.create(name='Test Album', year=2023, artist='Test Artist', user=user)
    response = client.post(reverse('album_delete', args=[album.id]))
    assert response.status_code == 302  # Redirect after successful deletion
    assert not Album.objects.filter(id=album.id).exists()

@pytest.mark.django_db
def test_homepage_welcome_message(client):
    user = User.objects.create_user(username='testuser', password='testpassword')
    response = client.get(reverse('review_list'))
    assert 'Welcome to StarTrax' in response.content.decode()
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('review_list'))
    assert f'Welcome back, {user.username}' in response.content.decode()

@pytest.mark.django_db
def test_navigation_links(client):
    response = client.get(reverse('review_list'))
    assert response.status_code == 200
    assert reverse('login') in response.content.decode()
    assert reverse('register') in response.content.decode()
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    response = client.get(reverse('review_list'))
    assert reverse('logout') in response.content.decode()