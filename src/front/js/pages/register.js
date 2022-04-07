/* import { useContext, useState } from "react";
import { Context } from "../store/appContext";

export const Register = () => {
  const store = useContext(Context);
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
  });

  const [error, setError] = useState(null);

  const validatePassword = (password) => {
    console.log(password, typeof password, password.length);
    if (password.length <= 6) {
      setError("Tu contraseña debe tener mas de 7 caracteres");
    } else {
      setError(null);
    }
    return;
  };

  const validateEmail = (email) => {
    const regex =
      /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (!email.match(regex)) {
      setError("Tu email debe tener un formato válido");
    }
    return email.toLowerCase();
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
    validatePassword(formData.password);
    const parseEmail = validateEmail(formData.email);
    store.actions.register_user(formData);
  };
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };
 */

import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

export const Register = () => {
  const store = useContext(Context);
  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
  });
  const [error, setError] = useState(null);

  const validatePassword = (password) => {
    console.log(password, typeof password, password.length);
    if (password.length <= 6) {
      setError("Tu contraseña debe tener mas de 7 caracteres");
    } else {
      setError(null);
    }
    return;
  };

  const validateEmail = (email) => {
    const regex =
      /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (!email.match(regex)) {
      setError("Tu email debe tener un formato válido");
    }
    return email.toLowerCase();
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
    validatePassword(formData.password);
    const parseEmail = validateEmail(formData.email);
    store.actions.register_user(formData);
  };
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <div className="container">
      <div className="row">
        <div className="col-md-6 mt-5 mx-auto">
          {<label> {error && error}</label>}
          <form noValidate onSubmit={handleSubmit}>
            <h1 className="h3 mb-3 font-weight-normal"> Registro</h1>
            <div className="form-group">
              <label htmlFor="first_name">Primer nombre</label>
              <input
                type="text"
                className="form-control"
                name="first_name"
                placeholder="nombre"
                value={formData.first_name}
                onChange={handleChange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="last_name">Apellidos</label>
              <input
                type="text"
                className="form-control"
                name="last_name"
                placeholder="Apellidos"
                value={formData.last_name}
                onChange={handleChange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="email">Correo electrónico</label>
              <input
                type="text"
                className="form-control"
                name="email"
                placeholder="email"
                value={formData.email}
                onChange={handleChange}
              />
            </div>
            <div className="form-group">
              <label htmlFor="password">password</label>
              <input
                type="text"
                className="form-control"
                name="password"
                placeholder="password"
                value={formData.password}
                onChange={handleChange}
              />
            </div>
            <button type="submit" className="btn btn-lg btn-success btn-block">
              Registrate
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};
