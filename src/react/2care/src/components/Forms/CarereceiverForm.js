import React, { useState } from "react";
import { registerCarereceiver } from '../../services/authService';

const CarereceiverForm = () => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    confirm_password: "",
    name: "",
    birth_date: "",
    language: "",
    contact_number: "",
    gender: "",
    address: "",
    special_care: "",
    share_special_care: false,
    emergency_contact: "",
    additional_info: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await registerCarereceiver(formData);
      console.log("Usuário registrado com sucesso");
      
    } catch (error) {
      console.error("Erro ao cadastrar os dados:", error.message);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="columnLeft50">
        <div className="field">
          <label htmlFor="email">Email:</label>
          <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} required></input>
        </div>
        <div className="field">
          <label htmlFor="password">password:</label>
          <input type="password" id="password" name="password" value={formData.password} onChange={handleChange} required></input>
        </div>
        <div className="field">
          <label htmlFor="confirm_password">Confirmar senha:</label>
          <input type="password" id="confirm_password" name="confirm_password" value={formData.confirm_password} onChange={handleChange} required></input>
        </div>
        <div className="field">
          <label htmlFor="name">Nome completo:</label>
          <input type="text" id="name" name="name" value={formData.name} onChange={handleChange} required></input>
        </div>
        <div className="field">
          <label htmlFor="birth_date">Data de Nascimento:</label>
          <input type="date" id="birth_date" name="birth_date" value={formData.birth_date} onChange={handleChange} ></input>
        </div>
        <div className="field">
          <label htmlFor="language">Idioma:</label>
          <select id="language" name="language" value={formData.language} onChange={handleChange}>
            <option value="portugues">Português</option>
            <option value="ingles">Inglês</option>
            <option value="espanhol">Espanhol</option>
          </select>
        </div>
        <div className="field">
          <label htmlFor="contact_number">Telefone/Celular:</label>
          <input type="tel" id="contact_number" name="contact_number" value={formData.contact_number} onChange={handleChange}></input>
        </div>
        <div className="field">
          <label htmlFor="gender">Gênero:</label>
          <select id="gender" name="gender" value={formData.gender} onChange={handleChange}>
            <option value="masculino">Masculino</option>
            <option value="feminino">Feminino</option>
            <option value="outro">Outro</option>
          </select>
        </div>
      </div>
      <div className="columnRight50">
        <div className="field">
          <label htmlFor="address">Localização:</label>
          <input type="text" id="address" name="address" value={formData.address} onChange={handleChange}></input>
        </div>
        <div className="field">
          <label htmlFor="special_care">Cuidados Especiais:</label>
          <input type="text" id="special_care" name="special_care" value={formData.special_care} onChange={handleChange}></input>
        </div>
        <div>
          <input type="checkbox" className="checkbox" id="share_special_Care" name="share_special_Care" value={formData.share_special_care} onChange={handleChange}></input>
          <label htmlFor="share_special_Care">Aceito compartilhar cuidados especiais</label>
        </div>
        <div className="field">
          <label htmlFor="emergency_contact">Contatos de Emergência:</label>
          <input type="text" id="emergency_contact" name="emergency_contact" value={formData.emergency_contact} onChange={handleChange}></input>
        </div>
        <div className="field">
          <label htmlFor="additional_info">Informações Adicionais:</label>
          <textarea id="additional_info" name="additional_info" value={formData.additional_info} onChange={handleChange}></textarea>
        </div>
      </div>
      <button type="submit">Salvar</button>
    </form>
  );
};

export default CarereceiverForm;