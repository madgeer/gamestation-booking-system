import React, { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import { Calendar, Clock, User, Mail, Gamepad } from 'lucide-react';
import './Booking.css';

const Booking = () => {
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const stationFromUrl = queryParams.get('station');

  const [formData, setFormData] = useState({
    name: '',
    email: '',
    date: '',
    time: '',
    duration: '2',
    station: stationFromUrl || 'pro-pc'
  });

  const [isSubmitted, setIsSubmitted] = useState(false);

  // Auto-scroll to top when page loads
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Simulate API call
    setTimeout(() => {
      setIsSubmitted(true);
    }, 1000);
  };

  if (isSubmitted) {
    return (
      <div className="booking-page success-page">
        <div className="container">
          <div className="glass-panel success-card animate-fade-in">
            <div className="success-icon">✓</div>
            <h2>Booking Confirmed!</h2>
            <p>Thank you, {formData.name}. Your booking for the <strong>{formData.station.replace('-', ' ')}</strong> setup has been successfully received.</p>
            <div className="booking-details-summary">
              <p><strong>Date:</strong> {formData.date}</p>
              <p><strong>Time:</strong> {formData.time}</p>
              <p><strong>Duration:</strong> {formData.duration} Hours</p>
            </div>
            <button className="btn btn-primary mt-4" onClick={() => window.location.href = '/'}>
              Return Home
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="booking-page">
      <div className="container">
        <div className="booking-header text-center animate-fade-in">
          <h1 className="section-title">Book Your <span className="text-gradient">Session</span></h1>
          <p className="section-subtitle">Reserve your preferred gaming station ahead of time to guarantee availability.</p>
        </div>

        <div className="booking-content glass-panel animate-fade-in delay-1">
          <form className="booking-form" onSubmit={handleSubmit}>
            
            <div className="form-section">
              <h3>Personal Information</h3>
              <div className="form-row">
                <div className="form-group">
                  <label><User size={16} /> Full Name</label>
                  <input 
                    type="text" 
                    name="name" 
                    value={formData.name} 
                    onChange={handleChange} 
                    required 
                    placeholder="John Doe"
                  />
                </div>
                <div className="form-group">
                  <label><Mail size={16} /> Email Address</label>
                  <input 
                    type="email" 
                    name="email" 
                    value={formData.email} 
                    onChange={handleChange} 
                    required 
                    placeholder="john@example.com"
                  />
                </div>
              </div>
            </div>

            <div className="form-section">
              <h3>Session Details</h3>
              <div className="form-row">
                <div className="form-group">
                  <label><Gamepad size={16} /> Select Station</label>
                  <select 
                    name="station" 
                    value={formData.station} 
                    onChange={handleChange}
                  >
                    <option value="pro-pc">Pro PC Setup ($5/hr)</option>
                    <option value="elite-pc">Elite PC Setup ($8/hr)</option>
                    <option value="console-lounge">Console Lounge ($10/hr)</option>
                  </select>
                </div>
                <div className="form-group">
                  <label><Clock size={16} /> Duration (Hours)</label>
                  <select 
                    name="duration" 
                    value={formData.duration} 
                    onChange={handleChange}
                  >
                    <option value="1">1 Hour</option>
                    <option value="2">2 Hours</option>
                    <option value="3">3 Hours</option>
                    <option value="4">4 Hours</option>
                    <option value="5">5+ Hours (Day Pass)</option>
                  </select>
                </div>
              </div>
              
              <div className="form-row">
                <div className="form-group">
                  <label><Calendar size={16} /> Date</label>
                  <input 
                    type="date" 
                    name="date" 
                    value={formData.date} 
                    onChange={handleChange} 
                    required 
                  />
                </div>
                <div className="form-group">
                  <label><Clock size={16} /> Time</label>
                  <input 
                    type="time" 
                    name="time" 
                    value={formData.time} 
                    onChange={handleChange} 
                    required 
                  />
                </div>
              </div>
            </div>

            <div className="booking-summary">
              <div className="summary-info">
                <h4>Order Summary</h4>
                <p>You are booking a <strong>{formData.duration} hour(s)</strong> session.</p>
                <p>Payment will be collected at the front desk upon arrival.</p>
              </div>
              <button type="submit" className="btn btn-primary submit-btn">
                Confirm Booking
              </button>
            </div>
            
          </form>
        </div>
      </div>
    </div>
  );
};

export default Booking;
