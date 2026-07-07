import os
import re

new_footer = '''        <footer class="site-footer">
            <div class="container">
                <div class="site-footer__top">
                    <div class="site-footer__top-left">
                        <h3>Planet Green plays a great role and a sample text goes here</h3>
                    </div>
                    <div class="site-footer__top-right">
                        <p class="site-footer__newsletter-title">Get in touch with our team</p>
                        <div class="footer-widget">
                            <form class="mc-form" action="#">
                                <input type="email" placeholder="Enter your email" required>
                                <button type="submit">Subscribe</button>
                            </form>
                        </div>
                    </div>
                </div>
        
                <div class="row site-footer__widgets">
                    <div class="col-sm-12 col-md-6 col-lg-3">
                        <h3 class="footer-widget__title">Quick Links</h3>
                        <ul class="list-unstyled footer-widget__links">
                            <li><a href="about.html">About</a></li>
                            <li><a href="services.html">Services</a></li>
                            <li><a href="contact.html">Contact</a></li>
                            <li><a href="blog.html">Blogs</a></li>
                        </ul>
                    </div>
        
                    <div class="col-sm-12 col-md-6 col-lg-3">
                        <h3 class="footer-widget__title">UAE</h3>
                        <ul class="list-unstyled footer-widget__contact">
                            <li>
                                <i class="pg-icon-pin"></i>
                                <a href="#">Office No: OFF2-0113, Ras Al Khor Industrial Area 3rd, Bur Dubai</a>
                            </li>
                            <li>
                                <i class="pg-icon-telephone"></i>
                                <a href="tel:+971 50-355-7600">+971 50-355-7600</a>
                            </li>
                        </ul>
                    </div>
        
                    <div class="col-sm-12 col-md-6 col-lg-3">
                        <h3 class="footer-widget__title">KSA</h3>
                        <ul class="list-unstyled footer-widget__contact">
                            <li>
                                <i class="pg-icon-pin"></i>
                                <a href="#">Office No: OFF2-0113, Ras Al Khor Industrial Area 3rd, Bur Dubai</a>
                            </li>
                            <li>
                                <i class="pg-icon-telephone"></i>
                                <a href="tel:+971 50-355-7600">+971 50-355-7600</a>
                            </li>
                        </ul>
                    </div>
        
                    <div class="col-sm-12 col-md-6 col-lg-3 site-footer__logo-col">
                        <img src="assets/images/icons/Icon_v.png" class="site-footer__watermark" alt="Planet Green">
                    </div>
                </div>
        
                <div class="site-footer__bottom" style="text-align: right; border-top: 0; margin-top: 0;">
                    <p>© Copyright 2026 Planet Green</p>
                </div>
            </div>
        </footer>'''

files = ['about.html', 'blog.html', 'contact.html', 'blog-details-1.html', 'blog-details-2.html', 'blog-details-3.html']

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the old footer
        pattern = r'<footer class="site-footer" style="margin: auto;">.*?<div class="bottom-footer">.*?</div>\s*</div>'
        new_content = re.sub(pattern, new_footer, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {file}')
        else:
            print(f'No match found in {file}')
