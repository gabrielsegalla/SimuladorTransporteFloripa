import React from "react";
import PropTypes from "prop-types";
import "./styles.css";

const SelectDestiny = ({ id, name, options, onChange }) => {
  return (
    <select id={id} name={name} className={"select"} onChange={onChange}>
      { options &&
      <>
      {options.map((region, index) => {
        return (
          <option id={index} key={index} value={region.region}>
            {region.name}
          </option>
        );
      })}
      </>
      }
    </select>
  );
};

SelectDestiny.propTypes = {
  id: PropTypes.string,
  name: PropTypes.string,
  options: PropTypes.arrayOf(PropTypes.object).isRequired,
  onChange: PropTypes.func
};

export default SelectDestiny;
