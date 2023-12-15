// App.js
import React from 'react';
import Navbar from './Navbar'; // Adjust the path based on the actual location of Navbar.js
import CarouselWithContent from "./Carousel.js";
import ButtonWithInput from './ButtonWithInput.js';
import Banner from './Banner.js';


function App() {
  return (
    <div>
      <Navbar />
      <Banner/>
      {/* <CarouselWithContent/>
      <ButtonWithInput/> */}
      {/* Your main content goes here */}
    </div>
  );
}

export default App;
