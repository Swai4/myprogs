<input type="text" name="name" class="input" placeholder="Enter Your Name">
                    <input type="text" name="name" class="input" placeholder="Enter Your Email">
                    <textarea name="msg" id="msg" cols="30" rows="10" placeholder="Enter your Message"></textarea>


{{ message }}
                        {% if messages %}
                        {% for message in messages %}
                                <i>{{ message }}!</i>
                        {% endfor %}
                        {% endif %}