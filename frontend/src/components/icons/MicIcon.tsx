import * as React from "react";

const MicIcon = (props: React.SVGProps<SVGSVGElement>) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width={24}
    height={24}
    fill="currentColor"
    viewBox="0 0 24 24"
    {...props}
  >
    <path
      fillRule="evenodd"
      d="M7 7a5 5 0 0 1 10 0v4a5 5 0 0 1-10 0V7Zm5-3a3 3 0 0 0-3 3v4a3 3 0 1 0 6 0V7a3 3 0 0 0-3-3Z"
      clipRule="evenodd"
    />
    <path d="M11 19.945V21a1 1 0 1 0 2 0v-1.055a9.008 9.008 0 0 0 7.345-5.57 1 1 0 0 0-1.854-.75A7.002 7.002 0 0 1 12 18h-.003a7.003 7.003 0 0 1-6.489-4.375 1 1 0 1 0-1.853.75A9.008 9.008 0 0 0 11 19.945Z" />
  </svg>
);

export default MicIcon;
