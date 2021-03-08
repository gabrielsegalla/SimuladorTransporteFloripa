import React from "react";
import "./styles.css";
import PropTypes from "prop-types";

const Button = ({ children, outlined, id, onClick }) => {
  return (
    <button
      id={id}
      className={`button ${outlined && "outlined"}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
};

Button.propTypes = {
  children: PropTypes.any,
  outlined: PropTypes.bool,
  id: PropTypes.string,
  onClick: PropTypes.func
};

export default Button;
