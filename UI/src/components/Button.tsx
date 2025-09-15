export default function Button({
  className,
  label,
  onClick,
}: {
  className?: string;
  label: string;
  onClick: () => void;
}) {
  return (
    <button
      className={`${className} bg-blue-500 hover:drop-shadow-[0_0_10px_#06b6d4] text-white text-md font-bold py-2 px-4 rounded`}
      onClick={(e) => {
        e.preventDefault();
        onClick();
      }}
    >
      {label}
    </button>
  );
}
