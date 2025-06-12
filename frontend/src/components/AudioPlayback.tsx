import { motion } from "motion/react";

import { cn } from "@/components/ui/utils";

export function AudioPlayback({
  playbackFrequencies,
  itemClassName,
  className,
  height = 36,
}: {
  playbackFrequencies: number[];
  itemClassName?: string;
  className?: string;
  height?: number;
}) {
  return (
    <div
      className={cn(`flex items-center justify-center gap-[2px]`, className)}
    >
      {playbackFrequencies.map((frequency: number, index: number) => (
        <motion.div
          key={index}
          className={cn("w-[4px] sm:w-[6px] rounded", itemClassName)}
          initial={{ height: 0 }}
          animate={{ height: `${frequency * height}px` }}
          transition={{ duration: 0.2, ease: "easeOut" }}
        />
      ))}
    </div>
  );
}
