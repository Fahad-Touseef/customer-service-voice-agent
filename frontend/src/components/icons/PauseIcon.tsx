import * as React from "react";

const PauseIcon = (props: React.SVGProps<SVGSVGElement>) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width={24}
    height={24}
    fill="currentColor"
    viewBox="0 0 24 24"
    {...props}
  >
    <path d="M6 8a2 2 0 0 1 2-2h.5a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V8Zm7.5 0a2 2 0 0 1 2-2h.5a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2h-.5a2 2 0 0 1-2-2V8Z" />
  </svg>
);

export default PauseIcon;
