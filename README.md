# Event Captcha
### Access **[Event Captcha](https://eventcaptcha.fly.dev/)**

![Screenshot of Login](/main_app/static/images/login.png)
![Screenshot of the Event Details Page](/main_app/static/images/image-2.png)
![Screenshot of Event Details Page](/main_app/static/images/details.png)


### About The App:

Welcome to Event Captcha, a platform that helps you organize and track all your events. Whether you're planning upcoming gatherings or reminiscing about past events, Event Collector is your ultimate digital scrapbook for every moment. Say goodbye to the hassle of forgetting memorable occasions and missing out on exciting future plans.





### App Highlights:

Welcome to Event Captcha, the all-in-one digital scrapbook for every event throughout your life's journey, whether it's in the past, happening now, or awaiting in the future. With Event Captcha, managing events becomes a breeze, enabling you to effortlessly preserve and organize your cherished memories.

### Key Features:

1. **Capture the Magic 📸:** Record your thoughts to preserve the essence of every event you attend. From epic concerts and family gatherings to exciting vacations and future plans.

2. **Chronicle Your Journey 🌟:** Create a captivating and fun chronicle of your event-filled life. Easily organize and revisit past events, anticipate upcoming adventures, and reflect on the wonderful tapestry of your experiences.

3. **Never Miss a Beat 📅:** Stay on top of your event schedule with built-in reminders and calendars. Whether it's a concert, wedding, or a simple meet-up with friends.


These highlights are designed to make Event Captcha your go-to event management companion. Start capturing your moments today!
#### Fun Dev Highlight: Dynamically Rendered Category Images

Enhance your event management experience with our latest feature that adds a delightful and visual touch to your events. By implementing automatic event image display based on the selected category when you create an event. Here's how we achieved this:

**Step 1: HTML Code:**
``````
<div class="card-img-container">
  {% with category_code=event.category %}
    <img 
      src="{% static 'images/category_images/' %}{% if category_code %}{{ category_code }}.png{% else %}default.png{% endif %}"
      alt="Category: {{ event.get_category_display }}"
    >
  {% endwith %}
</div>
``````
**Step 2: Ensure there was an is image to match each category:**
![Category Images Directory Screenshot](/main_app/static/images/categories.png)


**Supported Categories:**
``````
CATEGORIES = (
  ('AR', 'Art'),
  ('CH', 'Charity'),
  ('CM', 'Comedy Show'),
  ('CN', 'Conference'),
  ('CO', 'Concert'),
  ('CS', 'Class / Seminar'),
  ('EX', 'Exercise / Fitness'),
  ('FA', 'Fashion'),
  ('FE', 'Festival'),
  ('FI', 'Film'),
  ('FO', 'Food'),
  ('FU', 'Fundraiser'),
  ('GA', 'Gala'),
  ('MU', 'Music'),
  ('NE', 'Networking'),
  ('OT', 'Other'),
  ('PA', 'Party'),
  ('SP', 'Sports'),
  ('TH', 'Theater'),
  ('WE', 'Wedding'),
  ('WR', 'Work Outing'),
)
``````

**A glimpse of how it looks:**
![Event List Screenshot](/main_app/static/images/image-1.png)


## Technologies Used:

- Python
- Docker Container
- PostgreSQL
- Django
- Neon
- Fly.io
- HTML
- CSS
- JavaScript
- Database (e.g., SQLite)
- Frameworks and libraries (e.g., Django REST framework)

## Attributions:

- Favicon - [Event Icon](https://icons8.com/icon/fTBV7GkKahC6/event) from Icons8.
- Gradient Background - 003 Spring Warmth from [CSS Gradient](https://cssgradient.io/gradient-backgrounds/)
- Logo & Category Images created using Canva Pro.
- H1 Font - [Rancho](https://fonts.google.com/specimen/Rancho) from Google Font
---

## ❄️ Icebox Features 🧊

Explore these upcoming features that we're excited to introduce:

- [ ] **Note Section**: We're working on adding a dedicated note section for each event. Keep track of important details and memories associated with your events.

- [ ] **Event Photo Upload**: Share your experiences with event photos. Upload and display images to capture the essence of your events.

- [ ] **Event Collections**: Organize your events with ease. Create event collections, such as "Trip To XYZ," and link related events for better event management.

- [ ] **Event Sharing**: Invite friends to join your events by sharing them seamlessly. Whether it's a small gathering or a grand celebration, this feature will make collaboration a breeze.


---

🚀 Stay tuned for updates, and feel free to share your ideas and feedback with us! Thank you for choosing Event Collector as your event tracking and management tool. 