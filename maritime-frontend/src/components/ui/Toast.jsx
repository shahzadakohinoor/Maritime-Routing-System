/**
 * Toast Component
 * Props:
 * - message: notification message
 */

function Toast({ message }) {
  return <div className="ui-toast">{message}</div>;
}

export default Toast;