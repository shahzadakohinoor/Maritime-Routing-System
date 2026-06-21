/**
 * Modal Component
 * Props:
 * - title: modal heading
 * - children: modal body content
 * - onClose: close function
 */

function Modal({ title, children, onClose }) {
  return (
    <div className="ui-modal-backdrop">
      <div className="ui-modal">
        <button className="ui-modal-close" onClick={onClose}>
          ×
        </button>
        <h3>{title}</h3>
        <div>{children}</div>
      </div>
    </div>
  );
}

export default Modal;