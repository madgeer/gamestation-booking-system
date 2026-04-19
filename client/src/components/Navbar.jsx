import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Gamepad2, Menu, X } from 'lucide-react';
import './Navbar.css';

const Navbar = () => {
  const [scrolled, setScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const location = useLocation();

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Close mobile menu on route change
  useEffect(() => {
    setMobileMenuOpen(false);
  }, [location]);

  return (
    <nav className={`navbar ${scrolled ? 'scrolled' : ''}`}>
      <div className="container nav-container">
        <Link to="/" className="nav-logo">
          <Gamepad2 size={32} className="logo-icon" />
          <span className="logo-text text-gradient">NEXUS</span>
        </Link>

        <div className="nav-links desktop-only">
          <Link to="/" className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}>Home</Link>
          <a href="/#stations" className="nav-link">Stations</a>
          <a href="/#pricing" className="nav-link">Pricing</a>
          <Link to="/booking" className="btn btn-primary nav-btn">Book Now</Link>
        </div>

        <button 
          className="mobile-menu-btn mobile-only"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
        >
          {mobileMenuOpen ? <X size={28} /> : <Menu size={28} />}
        </button>
      </div>

      {/* Mobile Menu */}
      <div className={`mobile-menu glass-panel ${mobileMenuOpen ? 'open' : ''}`}>
        <Link to="/" className="mobile-link">Home</Link>
        <a href="/#stations" className="mobile-link" onClick={() => setMobileMenuOpen(false)}>Stations</a>
        <a href="/#pricing" className="mobile-link" onClick={() => setMobileMenuOpen(false)}>Pricing</a>
        <Link to="/booking" className="btn btn-primary mobile-btn">Book Now</Link>
      </div>
    </nav>
  );
};

export default Navbar;
