import React from "react";
import CarouselWithContent from "./Carousel";
import ButtonWithInput from "./ButtonWithInput.js"

const Banner = () => {
    return (
      <div className="banner">
        {/* Left side with Carousel */}
        <div className="left-side">
          <CarouselWithContent />
        </div>
  
        {/* Right side with ButtonWithInput */}
        <div className="right-side">
          <ButtonWithInput title/>
        </div>
      </div>
    );
  };
  
  export default Banner;