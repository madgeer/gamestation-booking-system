import React from 'react';
import { Gamepad2, MessageSquare, Camera, Video } from 'lucide-react';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-grid">
          <div className="footer-brand">
            <div className="footer-logo">
              <Gamepad2 size={28} className="logo-icon" />
              <span className="logo-text text-gradient">NEXUS</span>
            </div>
            <p className="footer-desc">Premium gaming lounge for hardcore gamers, casual players, and esports enthusiasts. Experience the ultimate gaming setup.</p>
            <div className="social-links">
              <a href="#" className="social-link"><MessageSquare size={20} /></a>
              <a href="#" className="social-link"><Camera size={20} /></a>
              <a href="#" className="social-link"><Video size={20} /></a>
            </div>
          </div>
          
          <div className="footer-links">
            <h4>Quick Links</h4>
            <ul>
              <li><a href="/">Home</a></li>
              <li><a href="#stations">Stations</a></li>
              <li><a href="#pricing">Pricing</a></li>
              <li><a href="/booking">Book Now</a></li>
            </ul>
          </div>
          
          <div className="footer-links">
            <h4>Support</h4>
            <ul>
              <li><a href="#">FAQ</a></li>
              <li><a href="#">Contact Us</a></li>
              <li><a href="#">Terms of Service</a></li>
              <li><a href="#">Privacy Policy</a></li>
            </ul>
          </div>
          
          <div className="footer-contact">
            <h4>Visit Us</h4>
            <p>123 Cyber Street, Level 4<br />Neo Tokyo, NT 10001</p>
            <p className="mt-2">Open 24/7 for members</p>
          </div>
        </div>
        
        <div className="footer-bottom">
          <p>&copy; {new Date().getFullYear()} Nexus Gaming Lounge. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
