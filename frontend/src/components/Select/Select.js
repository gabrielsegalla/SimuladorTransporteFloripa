import React from "react";
import PropTypes from "prop-types";
import "./styles.css";

const Select = ({ id, name, options, onChange }) => {
  return (
    <select id={id} name={name} className={"select"} onChange={onChange}>
      { options &&
      <>
      {options.map((option, index) => {
        return (
          <option id={index} key={index} value={option.id}>
            {option.name}
          </option>
        );
      })}
      </>
      }
    </select>
  );
};

Select.propTypes = {
  id: PropTypes.string,
  name: PropTypes.string,
  options: PropTypes.arrayOf(PropTypes.object).isRequired,
  onChange: PropTypes.func
};

export default Select;
