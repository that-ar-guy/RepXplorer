import React, { useState, useEffect } from "react";
import { Carousel } from "@material-tailwind/react";
import b1 from "./images/b1.jpeg";
import b2 from "./images/b2.jpeg";
import b3 from "./images/b3.jpeg";

const CarouselWithContent = () => {
  const [currentSlide, setCurrentSlide] = useState(0);

  const handleChange = (index) => {
    setCurrentSlide(index);
  };

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentSlide((prevSlide) => (prevSlide + 1) % 3);
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex items-center justify-start h-full">
      <Carousel
        className="rounded-xl w-1/2 ml-14 py-10" // Adjust the width as needed
        activeIndex={currentSlide}
        loop
        interval={5000}
      >
        {/* Slide 1 */}
        <div className="relative h-full w-full" key="slide1">
          <img
            src={b1}
            alt="h"
            className="h-full w-full object-cover"
          />
          {/* ... (content for slide 1) */}
        </div>

        {/* Slide 2 */}
        <div className="relative h-full w-full" key="slide2">
          <img
            src={b2} 
            alt="h"
            className="h-full w-full object-cover"
          />
          {/* ... (content for slide 2) */}
        </div>

        {/* Slide 3 */}
        <div className="relative h-full w-full" key="slide3">
          <img
            src={b3} 
            alt="h"
            className="h-full w-full object-cover"
          />
          {/* ... (content for slide 3) */}
        </div>
      </Carousel>
    </div>
  );
};

export default CarouselWithContent;
