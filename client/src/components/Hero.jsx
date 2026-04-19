import React from 'react';
import { Link } from 'react-router-dom';
import { ChevronRight, Zap, Shield, MonitorPlay } from 'lucide-react';
import './Hero.css';

const Hero = () => {
  return (
    <div className="hero">
      <div className="hero-bg">
        <img src="/hero-bg.png" alt="Premium Game Station" />
        <div className="hero-overlay"></div>
      </div>
      
      <div className="container hero-container">
        <div className="hero-content">
          <div className="badge animate-fade-in">
            <Zap size={16} className="badge-icon" />
            <span>Next-Gen Gaming Experience</span>
          </div>
          
          <h1 className="hero-title animate-fade-in delay-1">
            Unleash Your <br />
            <span className="text-gradient">True Potential</span>
          </h1>
          
          <p className="hero-subtitle animate-fade-in delay-2">
            Experience gaming like never before. High-end rigs, ultra-low latency, and an atmosphere designed for champions. Book your premium station today.
          </p>
          
          <div className="hero-actions animate-fade-in delay-3">
            <Link to="/booking" className="btn btn-primary hero-btn">
              Book a Station <ChevronRight size={20} />
            </Link>
            <a href="#stations" className="btn btn-outline hero-btn">
              View Setups
            </a>
          </div>
          
          <div className="hero-stats animate-fade-in delay-3">
            <div className="stat-item glass-panel">
              <MonitorPlay className="stat-icon" size={24} />
              <div>
                <h4 className="stat-value">50+</h4>
                <p className="stat-label">Premium PCs</p>
              </div>
            </div>
            <div className="stat-item glass-panel">
              <Zap className="stat-icon" size={24} />
              <div>
                <h4 className="stat-value">1ms</h4>
                <p className="stat-label">Network Latency</p>
              </div>
            </div>
            <div className="stat-item glass-panel">
              <Shield className="stat-icon" size={24} />
              <div>
                <h4 className="stat-value">24/7</h4>
                <p className="stat-label">Secure Access</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Hero;
