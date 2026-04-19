import React from 'react';
import { Link } from 'react-router-dom';
import { Cpu, Monitor, Wifi, Headphones } from 'lucide-react';
import './Stations.css';

const stationsData = [
  {
    id: 'pro-pc',
    title: 'Pro PC Setup',
    price: '$5/hr',
    image: 'https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&q=80&w=800',
    specs: ['RTX 4080', 'Intel i9 13900K', '32GB DDR5', '240Hz Monitor']
  },
  {
    id: 'elite-pc',
    title: 'Elite PC Setup',
    price: '$8/hr',
    image: 'https://images.unsplash.com/photo-1598550476439-6847785fcea6?auto=format&fit=crop&q=80&w=800',
    specs: ['RTX 4090', 'AMD Ryzen 9 7950X', '64GB DDR5', '360Hz Monitor']
  },
  {
    id: 'console-lounge',
    title: 'Console Lounge',
    price: '$10/hr',
    image: 'https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?auto=format&fit=crop&q=80&w=800',
    specs: ['PS5 & Xbox Series X', '65" 4K OLED TV', 'Surround Sound', 'Comfortable Sofa']
  }
];

const Stations = () => {
  return (
    <section id="stations" className="stations-section">
      <div className="container">
        <div className="section-header text-center">
          <h2 className="section-title">Premium <span className="text-gradient">Gaming Stations</span></h2>
          <p className="section-subtitle">Choose the perfect setup for your gaming needs. All stations come with pre-installed popular games and high-speed fiber internet.</p>
        </div>

        <div className="stations-grid">
          {stationsData.map((station, index) => (
            <div key={station.id} className="station-card glass-panel animate-fade-in" style={{animationDelay: `${index * 0.2}s`}}>
              <div className="station-image">
                <img src={station.image} alt={station.title} />
                <div className="station-price">{station.price}</div>
              </div>
              <div className="station-content">
                <h3>{station.title}</h3>
                <ul className="station-specs">
                  <li><Cpu size={16} className="spec-icon" /> {station.specs[0]}</li>
                  <li><Cpu size={16} className="spec-icon" /> {station.specs[1]}</li>
                  <li><Monitor size={16} className="spec-icon" /> {station.specs[2]}</li>
                  <li><Monitor size={16} className="spec-icon" /> {station.specs[3]}</li>
                </ul>
                <Link to={`/booking?station=${station.id}`} className="btn btn-outline w-100 mt-4">
                  Book Now
                </Link>
              </div>
            </div>
          ))}
        </div>
        
        <div className="features-grid mt-5">
          <div className="feature-item">
            <div className="feature-icon-wrapper"><Wifi size={24} /></div>
            <h4>Gigabit Internet</h4>
            <p>Ultra-low latency for competitive gaming.</p>
          </div>
          <div className="feature-item">
            <div className="feature-icon-wrapper"><Headphones size={24} /></div>
            <h4>Premium Peripherals</h4>
            <p>Top-tier mice, keyboards, and headsets included.</p>
          </div>
          <div className="feature-item">
            <div className="feature-icon-wrapper"><Monitor size={24} /></div>
            <h4>High Refresh Rates</h4>
            <p>Silky smooth gameplay on 240Hz+ monitors.</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Stations;
