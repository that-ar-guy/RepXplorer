import React from "react";
import { Navbar, Typography } from "@material-tailwind/react";

const NavbarComponent = () => {
  return (
    <Navbar
      variant="gradient" 
      color="black"
      className="mx-auto max-w-full bg-gradient-to-r from-black to-red-900 px-8 py-3 rounded-none"
    >
      <div className="flex flex-wrap items-center justify-between gap-y-4 text-white">
        <Typography
          as="a"
          href="#"
          variant="h3"
          className="mr-4 ml-2 cursor-pointer py-1.5"
        >
          RepXplorer
        </Typography>
        
      </div>
    </Navbar>
  );
}

export default NavbarComponent;
