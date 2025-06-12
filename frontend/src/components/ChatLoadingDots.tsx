import React from "react";
import { motion } from "motion/react";

export default function ChatLoadingDots() {
  return (
    <div
      className="flex items-center p-4 absolute bottom-0 pb-8"
      role="status"
      aria-live="polite"
    >
      <motion.span
        className="w-2.5 h-2.5 bg-gray-800 rounded-full"
        animate={{ opacity: [0.2, 1, 0.2] }}
        transition={{ duration: 1, repeat: Infinity, ease: "easeInOut" }}
      />
      <motion.span
        className="w-2.5 h-2.5 bg-gray-800 rounded-full mx-1"
        animate={{ opacity: [0.2, 1, 0.2] }}
        transition={{
          duration: 1,
          repeat: Infinity,
          ease: "easeInOut",
          delay: 0.2,
        }}
      />
      <motion.span
        className="w-2.5 h-2.5 bg-gray-800 rounded-full"
        animate={{ opacity: [0.2, 1, 0.2] }}
        transition={{
          duration: 1,
          repeat: Infinity,
          ease: "easeInOut",
          delay: 0.4,
        }}
      />
      <span className="sr-only">Loading...</span>
    </div>
  );
}
